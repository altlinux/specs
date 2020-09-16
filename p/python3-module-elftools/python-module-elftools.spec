%global commitdate 20130619
%global commit a1d968102e82fea06692c367849bc25418780f77
%global shortcommit a1d9681

%define oname elftools

%def_disable check

Name: python3-module-%oname
Version: 0.22
Release: alt2.git%commitdate.%shortcommit
Summary: Pure-Python library for parsing and analyzing ELF files

License: Public Domain
Group: Development/Python3
Url: https://github.com/eliben/%name

# We 'll use git snapshots, because upstream keeps master-branch
# in a usable, working state.  See:
# https://github.com/eliben/pyelftools/wiki/Hacking-guide#contributing
Packager: Lenar Shakirov <snejok@altlinux.ru>

Source: %oname-%version.tar

Patch: pyelftools-0.22-construct.patch

BuildArch: noarch

Requires: python3-module-construct
Provides: %name = %version-%release
Conflicts: python-module-elftools < %EVR
Obsoletes: python-module-elftools < %EVR

BuildRequires: python3-devel python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-construct

%description
Pure-Python library for parsing and analyzing ELF files
and DWARF debugging information.

%prep
%setup -n %oname-%version
%patch -p1

# remove bundled construct lib
rm -rf elftools/construct

%build
%python3_build

%install
%python3_install
mv %buildroot%_bindir/readelf.py %buildroot%_bindir/pyreadelf

%check
%__python3 test/run_all_unittests.py
%__python3 test/run_examples_test.py
# tests may fail because of differences in output-formatting
# from binutils' readelf.  See:
# https://github.com/eliben/pyelftools/wiki/Hacking-guide#tests
%__python3 test/run_readelf_tests.py || :

%files
%doc CHANGES LICENSE README* TODO
%python3_sitelibdir/*elftools*
%_bindir/pyreadelf

%changelog
* Thu Sep 17 2020 Grigory Ustinov <grenka@altlinux.org> 0.22-alt2.git20130619.a1d9681
- Drop python2 support.
- Disable check.

* Mon Dec 12 2016 Lenar Shakirov <snejok@altlinux.ru> 0.22-alt1.git20130619.a1d9681
- Initial build for ALT (based on 0.22-0.9.git20130619.a1d9681.fc25.src)
