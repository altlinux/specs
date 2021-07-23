%define _unpackaged_files_terminate_build 1

%define oname unicode_slugify

Name: python3-module-%oname
Version: 0.1.5
Release: alt4
Summary: A slugifier that works in unicode
License: BSD
BuildArch: noarch
Group: Development/Python3
Url: https://pypi.org/project/unicode-slugify

# https://github.com/mozilla/unicode-slugify.git
Source: %name-%version.tar
Patch1: %name-%version-alt.patch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3(six) python3(unidecode)
BuildRequires: python3-module-nose

%description
Unicode Slugify is a slugifier that generates unicode slugs.
It was originally used in the Firefox Add-ons web site
to generate slugs for add-ons and add-on collections.
Many of these add-ons and collections had
unicode characters and required more than simple transliteration.

%package tests
Summary: A slugifier that works in unicode
Group: Development/Python3
Requires: %name = %EVR

%description tests
Unicode Slugify is a slugifier that generates unicode slugs.
It was originally used in the Firefox Add-ons web site
to generate slugs for add-ons and add-on collections.
Many of these add-ons and collections had
unicode characters and required more than simple transliteration.

This package contains tests.

%prep
%setup
%patch1 -p1

%build
%python3_build

%install
%python3_install

%check
python3 setup.py test

%files
%doc README.md LICENSE
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/tests.*
%exclude %python3_sitelibdir/%oname/*/tests.*

%files tests
%python3_sitelibdir/%oname/tests.*
%python3_sitelibdir/%oname/*/tests.*

%changelog
* Fri Jul 23 2021 Grigory Ustinov <grenka@altlinux.org> 0.1.5-alt4
- Drop python2 support.

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 0.1.5-alt3
- NMU: remove rpm-build-ubt from BR:

* Sat Jun 15 2019 Igor Vlasenko <viy@altlinux.ru> 0.1.5-alt2
- NMU: remove %ubt from release

* Thu May 17 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 0.1.5-alt1%ubt
- Initial build for ALT.
