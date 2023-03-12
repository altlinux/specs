%define oname breathe
Name: python3-module-breathe
Version: 4.35.0
Release: alt1

Summary: Make reStructuredText and Sphinx read and render Doxygen xml output

License: BSD
Group: Development/Python3
Url: https://github.com/michaeljones/breathe

BuildArch: noarch

# Source0-url: %__pypi_url %oname
Source0: %oname-%version.tar

BuildRequires(pre): rpm-build-intro >= 2.2.4
BuildRequires(pre): rpm-build-python3

BuildRequires: python3-module-sphinx

#BuildRequires: python3-module-setuptools
Conflicts: python-module-breathe

%description
Breathe is an extension to reStructuredText and Sphinx to be able to read and render the Doxygen xml output.

%prep
%setup -n %oname-%version

%build
%python3_build

%install
%python3_install
# for compatibility
ln -s breathe-apidoc %buildroot/%_bindir/python3-breathe-apidoc

%files
%_bindir/breathe-apidoc
%_bindir/python3-breathe-apidoc
%python3_sitelibdir/*

%changelog
* Sun Mar 12 2023 Vitaly Lipatov <lav@altlinux.ru> 4.35.0-alt1
- new version 4.35.0 (with rpmrb script)

* Sun Jul 17 2022 Vitaly Lipatov <lav@altlinux.ru> 4.34.0-alt1
- new version 4.34.0 (with rpmrb script)

* Mon Apr 04 2022 Vitaly Lipatov <lav@altlinux.ru> 4.33.1-alt1
- new version 4.33.1 (with rpmrb script)

* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 4.30.0-alt1
- new version 4.30.0 (with rpmrb script)

* Sat Apr 24 2021 Vitaly Lipatov <lav@altlinux.ru> 4.29.1-alt1
- NMU: new version 4.29.1 (with rpmrb script)

* Sat Apr 24 2021 Vitaly Lipatov <lav@altlinux.ru> 4.7.3-alt2
- NMU: build python3 module separately, cleanup spec

* Tue Feb 20 2018 Fr. Br. George <george@altlinux.ru> 4.7.3-alt1
- Autobuild version bump to 4.7.3

* Fri Aug 25 2017 Fr. Br. George <george@altlinux.ru> 4.7.2-alt1
- Autobuild version bump to 4.7.2

* Mon Mar 13 2017 Fr. Br. George <george@altlinux.ru> 4.6.0-alt1
- Autobuild version bump to 4.6.0

* Mon Jul 11 2016 Fr. Br. George <george@altlinux.ru> 4.2.0-alt1
- Initial build for ALT

