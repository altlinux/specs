# TODO: check for release

%define oname psd2svg

%def_without check

Name: python3-module-%oname
Version: 0.2.3
Release: alt1

Summary: PSD to SVG converter based on psd-tools and svgwrite

License: MIT
Group: Development/Python3
Url: https://github.com/kyamagu/psd2svg

# Source-url: https://github.com/kyamagu/psd2svg/archive/master.zip
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro
BuildRequires(pre): rpm-build-python3

# TODO: epm restore
%py3_use Pillow
%py3_use svgwrite
%py3_use numpy
%py3_use psd-tools >= 1.8.11
%py3_use future

Provides: %oname

%description
psd2svg - PSD to SVG converter based on psd-tools and svgwrite.

%prep
%setup
# pytest-runner is deprecated
%__subst "s|.*setup_requires.*||" setup.py

%build
%python3_build_debug

%install
%python3_install

%check
%if_with check
%python3_check
%endif

%files
%doc *.rst
%_bindir/%oname
%python3_sitelibdir/%oname-%version-py%_python3_version.egg-info/
%python3_sitelibdir/%oname/

%changelog
* Sat Aug 21 2021 Vitaly Lipatov <lav@altlinux.ru> 0.2.3-alt1
- add Provides: psd2svg

* Sat Oct 17 2020 Vitaly Lipatov <lav@altlinux.ru> 0.2.3-alt0.1
- new version (0.2.3) with rpmgs script

* Sat Oct 17 2020 Vitaly Lipatov <lav@altlinux.ru> 0.1.7-alt1
- initial build for ALT Sisyphus

