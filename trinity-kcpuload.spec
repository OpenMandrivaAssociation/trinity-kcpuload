%bcond clang 1

# TDE variables
%define tde_pkg kcpuload
%define tde_prefix /opt/trinity


%undefine __brp_remove_la_files
%define dont_remove_libtool_files 1
%define _disable_rebuild_configure 1

# fixes error: Empty %files file …/debugsourcefiles.list
%undefine _debugsource_template

%define tarball_name %{tde_pkg}-trinity


Name:			trinity-%{tde_pkg}
Version:		14.1.6
Release:		1
Summary:		CPU meter for Kicker [Trinity]
Group:			Applications/Utilities
URL:			http://www.trinitydesktop.org/

License:	GPLv2+


Source0:		https://mirror.ppa.trinitydesktop.org/trinity/releases/R%{version}/main/applications/utilities/%{tarball_name}-%{version}.tar.xz

BuildSystem:  cmake

BuildOption:    -DCMAKE_BUILD_TYPE="RelWithDebInfo"
BuildOption:    -DCMAKE_INSTALL_PREFIX=%{tde_prefix}
BuildOption:    -DSHARE_INSTALL_PREFIX=%{tde_prefix}/share
BuildOption:    -DWITH_ALL_OPTIONS=ON
BuildOption:    -DBUILD_ALL=ON
BuildOption:    -DBUILD_DOC=ON
BuildOption:    -DBUILD_TRANSLATIONS=ON
BuildOption:    -DWITH_GCC_VISIBILITY=%{!?with_clang:ON}%{?with_clang:OFF}

BuildRequires:	trinity-tdelibs-devel >= %{version}
BuildRequires:	trinity-tdebase-devel >= %{version}
BuildRequires:	trinity-tde-cmake >= %{version}

BuildRequires:	desktop-file-utils

BuildRequires:	gettext


%{!?with_clang:BuildRequires:	gcc-c++}

BuildRequires:	pkgconfig

# IDN support
BuildRequires:	pkgconfig(libidn)

# OPENSSL support
BuildRequires:  pkgconfig(openssl)


BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(ice)
BuildRequires:  pkgconfig(sm)


%description
KCPULoad is a small program for Kicker (the TDE panel).  It shows a
recent history of CPU usage in the form of one or two configurable
diagrams in the system tray.  These diagrams have settings for colours
and various different styles.

KCPULoad has support for SMP and separate user/system loads.


%conf -p
unset QTDIR QTINC QTLIB
export PATH="%{tde_prefix}/bin:${PATH}"
export PKG_CONFIG_PATH="%{tde_prefix}/%{_lib}/pkgconfig"


%install -a
%find_lang %{tde_pkg} || touch %{tde_pkg}.lang

# Fix desktop files (openSUSE only)
echo "OnlyShowIn=TDE;" >>"%{?buildroot}%{tde_prefix}/share/applications/tde/%{tde_pkg}.desktop"


%files -f %{tde_pkg}.lang
%defattr(-,root,root,-)
%{tde_prefix}/bin/kcpuload
%{tde_prefix}/share/applications/tde/kcpuload.desktop
%{tde_prefix}/share/apps/kcpuload/
%{tde_prefix}/share/icons/crystalsvg/*/apps/kcpuload.png
%{tde_prefix}/share/icons/locolor/*/apps/kcpuload.png
%{tde_prefix}/share/man/man1/*.1*
%{tde_prefix}/share/doc/tde/HTML/en/kcpuload/

