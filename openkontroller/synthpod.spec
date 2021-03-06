# Global variables for github repository
%global commit0 4995be8180731b802641d72f532063c3d7686af9
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

%global debug_package %{nil}

Name:         synthpod
Version:      0.1.0
Release:      2%{?dist}
Summary:      Lightweight Nonlinear LV2 Plugin Container
URL:          https://github.com/OpenMusicKontrollers/synthpod
Source0:      https://github.com/OpenMusicKontrollers/synthpod/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz
Group:        Applications/Multimedia
License:      GPLv2+

BuildRequires: lv2-devel
BuildRequires: lilv-devel
BuildRequires: sratom-devel
BuildRequires: nanomsg-devel
BuildRequires: efl-devel
BuildRequires: elementary-devel
BuildRequires: jack-audio-connection-kit-devel
BuildRequires: zita-alsa-pcmi-devel
BuildRequires: xcb-util-wm-devel
BuildRequires: mesa-libGL-devel
BuildRequires: libuv-devel
BuildRequires: meson
BuildRequires: cairo-devel
BuildRequires: qt-devel
BuildRequires: qt5-qtbase-devel

%description
Lightweight Nonlinear LV2 Plugin Container

%prep
%setup -qn %{name}-%{commit0}

%build

VERBOSE=1 meson --prefix=/usr build
cd build

DESTDIR=%{buildroot} VERBOSE=1 ninja 

%install 

cd build
DESTDIR=%{buildroot} ninja install

%files
%{_bindir}/*
%{_libdir}/*
%{_datarootdir}/*

%changelog
* Sat May 12 2018 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-2
- update to latest master
- switch to meson build
* Tue Oct 24 2017 Yann Collette <ycollette.nospam@free.fr> - 0.1.0-1
- update to latest master
* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 0.1.0
- Initial build
