%define oname arpeggio
%def_with check

Name: python3-module-%oname
Version: 2.0.0
Release: alt1

Summary: Parser interpreter based on PEG grammars written in Python
License: MIT
Group: Development/Python3
Url: https://github.com/igordejanovic/Arpeggio
BuildArch: noarch

Source0: Arpeggio-%version.tar.gz

# Automatically added by buildreq on Sun Apr 17 2022
# optimized out: alt-os-release fonts-font-awesome libgpg-error mpdecimal python3 python3-base python3-dev python3-module-Pygments python3-module-apipkg python3-module-attrs python3-module-babel python3-module-click python3-module-dateutil python3-module-ghp-import python3-module-importlib-metadata python3-module-iniconfig python3-module-jinja2 python3-module-markdown python3-module-markupsafe python3-module-mergedeep python3-module-mkdocs python3-module-packaging python3-module-pep517 python3-module-pkg_resources python3-module-pluggy python3-module-py python3-module-pyparsing python3-module-pytest python3-module-pytz python3-module-pyyaml-env-tag python3-module-six python3-module-tomli python3-module-verspec python3-module-watchdog python3-module-yaml python3-module-zipp sh4 xz
BuildRequires: python3-module-build python3-module-flit python3-module-mike python3-module-setuptools python3-module-wheel python3-module-pytest-runner


%if_with check
BuildRequires: pytest3
%endif

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
## python3 -c "import configparser; config = configparser.ConfigParser(); config.read('setup.cfg'); config['options']['setup_requires']=''; print(config['options']['setup_requires']); config.write(open('setup.cfg', 'w'))"

%build
python3 -m build -n -w
mkdocs build

%if_with check
%check
pytest3
%endif

%install
pip3 install --root=%buildroot --no-deps -I dist/Arpeggio-%version-*py3-none-any.whl

%files
%doc site examples
%python3_sitelibdir_noarch/%oname
%exclude %python3_sitelibdir_noarch/%oname/tests
%python3_sitelibdir_noarch/Arpeggio-*

%files tests
%python3_sitelibdir_noarch/%oname/tests

%changelog
* Sun Apr 17 2022 Fr. Br. George <george@altlinux.org> 2.0.0-alt1
- Autobuild version bump to 2.0.0
- Switch to modern build scheme
- Introduce tests

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

