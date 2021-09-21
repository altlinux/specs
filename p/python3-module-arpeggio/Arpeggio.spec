%define oname arpeggio

Name: python3-module-%oname
Version: 1.10.2
Release: alt1

Summary: Parser interpreter based on PEG grammars written in Python
License: MIT
Group: Development/Python3
Url: https://github.com/igordejanovic/Arpeggio
BuildArch: noarch

Source0: Arpeggio-%version.tar.gz

# Automatically added by buildreq on Mon Sep 06 2021
# optimized out: python3 python3-base python3-dev python3-module-Pygments python3-module-babel python3-module-click python3-module-dateutil python3-module-ghp-import python3-module-importlib-metadata python3-module-jinja2 python3-module-markdown python3-module-markupsafe python3-module-mergedeep python3-module-packaging python3-module-pkg_resources python3-module-pytz python3-module-pyyaml-env-tag python3-module-six python3-module-watchdog python3-module-yaml python3-module-zipp sh4 xz
BuildRequires: python3-module-mkdocs python3-module-pip python3-module-setuptools python3-module-wheel

%description
Arpeggio is a recursive descent parser with memoization based on PEG
grammars (aka Packrat parser).

%package tests
Summary: Test suite for %name
Group: Development/Python3
%description tests
%summary

%prep
%setup -n Arpeggio-%version
# A bit of hack here
python3 -c "import configparser; config = configparser.ConfigParser(); config.read('setup.cfg'); config['options']['setup_requires']=''; print(config['options']['setup_requires']); config.write(open('setup.cfg', 'w'))"

%build
%python3_build_debug -b build3

mkdocs build

%install
rm -rf build && ln -sf build3 build
%python3_install

%files
%doc site examples
%python3_sitelibdir_noarch/%oname
%exclude %python3_sitelibdir_noarch/%oname/tests
%python3_sitelibdir_noarch/Arpeggio-*.egg-info

%files tests
%python3_sitelibdir_noarch/%oname/tests

%changelog
* Tue Sep 21 2021 Fr. Br. George <george@altlinux.ru> 1.10.2-alt1
- Autobuild version bump to 1.10.2
- Separate tests submodule

* Wed Mar 24 2021 Grigory Ustinov <grenka@altlinux.org> 1.9.2-alt5
- Fixed FTBFS.

* Mon Jun 01 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.9.2-alt4
- Docs build fixed.

* Wed Feb 05 2020 Stanislav Levin <slev@altlinux.org> 1.9.2-alt3
- Fixed FTBS.

* Tue Nov 12 2019 Andrey Bychkov <mrdrew@altlinux.ru> 1.9.2-alt2
- disable python2

* Sat Oct 26 2019 Fr. Br. George <george@altlinux.ru> 1.9.2-alt1
- Autobuild version bump to 1.9.2

* Mon Jan 28 2019 Fr. Br. George <george@altlinux.ru> 1.9.0-alt1
- Autobuild version bump to 1.9.0

* Thu Jun 14 2018 Fr. Br. George <george@altlinux.ru> 1.8.0-alt1
- Autobuild version bump to 1.8.0

* Thu Jun 14 2018 Fr. Br. George <george@altlinux.ru> 1.7.1-alt1
- Initial build for ALT

