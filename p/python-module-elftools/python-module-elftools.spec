%def_with python3

%global commitdate 20130619
%global commit a1d968102e82fea06692c367849bc25418780f77
%global shortcommit a1d9681

Name: python-module-elftools
Version: 0.22
Release: alt1.git%commitdate.%shortcommit
Summary: Pure-Python library for parsing and analyzing ELF files

License: Public Domain
Group: Development/Python
Url: https://github.com/eliben/%name

# We 'll use git snapshots, because upstream keeps master-branch
# in a usable, working state.  See:
# https://github.com/eliben/pyelftools/wiki/Hacking-guide#contributing
Packager: Lenar Shakirov <snejok@altlinux.ru>

Source: %name-%version.tar

Patch: pyelftools-0.22-construct.patch

BuildArch: noarch

BuildRequires: rpm-build-python python-devel
BuildRequires: python-module-setuptools
BuildRequires: python-module-construct

Requires: python-module-construct
Provides: %name = %version-%release

%if_with python3
BuildRequires: python3-devel python3-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-construct
%endif

%description
Pure-Python library for parsing and analyzing ELF files
and DWARF debugging information.

%if_with python3
%package -n python3-module-elftools
Summary: Pure-Python library for parsing and analyzing ELF files
Group: Development/Python

Requires: python3-module-construct

%description -n python3-module-elftools
Pure-Python library for parsing and analyzing ELF files
and DWARF debugging information.
%endif

%prep
%setup
%patch0 -p1

# remove bundled construct lib
rm -rf elftools/construct

%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%if_with python3
pushd ../python3
%python3_install
popd
mv %buildroot%_bindir/readelf.py %buildroot%_bindir/python3-pyreadelf
%endif

%python_install
mv %buildroot%_bindir/readelf.py %buildroot%_bindir/pyreadelf

%check
%__python test/run_all_unittests.py
%__python test/run_examples_test.py
# tests may fail because of differences in output-formatting
# from binutils' readelf.  See:
# https://github.com/eliben/pyelftools/wiki/Hacking-guide#tests
%__python test/run_readelf_tests.py || :

%if_with python3
%__python3 test/run_all_unittests.py
%__python3 test/run_examples_test.py
# tests may fail because of differences in output-formatting
# from binutils' readelf.  See:
# https://github.com/eliben/pyelftools/wiki/Hacking-guide#tests
%__python3 test/run_readelf_tests.py || :
%endif

%files -n python-module-elftools
%doc CHANGES LICENSE README* TODO
%python_sitelibdir/*elftools*
%_bindir/pyreadelf

%if_with python3
%files -n python3-module-elftools
%doc CHANGES LICENSE README* TODO
%python3_sitelibdir/*elftools*
%_bindir/python3-pyreadelf
%endif

%changelog
* Mon Dec 12 2016 Lenar Shakirov <snejok@altlinux.ru> 0.22-alt1.git20130619.a1d9681
- Initial build for ALT (based on 0.22-0.9.git20130619.a1d9681.fc25.src)

