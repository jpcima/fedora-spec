# Global variables for github repository
%global commit0 e672d5feb9d631798e3d56eb96e8958c3d2c6821
%global gittag0 master
%global shortcommit0 %(c=%{commit0}; echo ${c:0:7})

# Disable production of debug package.
#%global debug_package %{nil}

Name:           mod-distortion
Version:        0.9.%{shortcommit0}
Release:        2%{?dist}
Summary:        mod-distortion LV2 set of plugins from portalmod

Group:          Applications/Multimedia
License:        GPLv2+
URL:            https://github.com/portalmod/mod-distortion
Source0:        https://github.com/portalmod/%{name}/archive/%{commit0}.tar.gz#/%{name}-%{shortcommit0}.tar.gz

BuildRequires: lv2-devel

%description
mod-distortion LV2 set of plugins from portalmod

%prep
%setup -qn %{name}-%{commit0}

%build
make INSTALL_PATH=%{buildroot}%{_libdir}/lv2 %{?_smp_mflags}

%install 
make INSTALL_PATH=%{buildroot}%{_libdir}/lv2 %{?_smp_mflags} install

%files
%{_libdir}/lv2/*

%changelog
* Sun May 13 2018 Yann Collette <ycollette.nospam@free.fr> - 0.9-2
- fix f27 / f28 build
* Sat Jun 06 2015 Yann Collette <ycollette.nospam@free.fr> - 0.9-1
- Initial build
