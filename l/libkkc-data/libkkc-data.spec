Group: Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-python3
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global debug_package %{nil}

Name:		libkkc-data
Version:	0.2.7
Release:	alt1_22
Epoch:		1
Summary:	Language model data for libkkc

License:	GPLv3+
URL:		https://github.com/ueno/libkkc/
Source0:	https://github.com/ueno/libkkc/releases/download/v0.3.5/%{name}-%{version}.tar.xz
Patch0:		https://github.com/ueno/libkkc/commit/ba1c1bd3eb86d887fc3689c3142732658071b5f7.patch

BuildRequires:	gcc
BuildRequires:	python3-devel
BuildRequires:	python3-module-marisa
Source44: import.info

%description
The %{name} package contains the language model data that libkkc uses
at run time.


%prep
%setup -q
%patch0 -p4 -b .orig


%build
export PYTHON=%{__python3}
%configure --disable-static
%make_build


%install
%makeinstall_std


%files
%doc COPYING
%{_libdir}/libkkc


%changelog
* Thu Sep 29 2022 Igor Vlasenko <viy@altlinux.org> 1:0.2.7-alt1_22
- new version

