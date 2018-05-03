%def_with python3

Name: z3
Version: 4.5.0
Release: alt1.1
Summary: High-performance theorem prover
License: MIT
Group: Sciences/Mathematics
Url: https://github.com/Z3Prover/z3

# https://github.com/Z3Prover/z3.git
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-make
BuildRequires: python-devel gcc-c++ doxygen graphviz libtau-devel
BuildRequires: python2.7(pkg_resources)

%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python-tools-2to3
BuildRequires: python3(pkg_resources)
%endif

%description
Z3 is a high-performance theorem prover being developed at Microsoft
Research.

%package -n lib%name
Summary: Shared library of %name
Group: System/Libraries

%description -n lib%name
Z3 is a high-performance theorem prover being developed at Microsoft
Research.

This package contains shared library of %name.

%package -n lib%name-devel
Summary: Development files of %name
Group: Development/C++
BuildArch: noarch
Requires: lib%name = %EVR

%description -n lib%name-devel
Z3 is a high-performance theorem prover being developed at Microsoft
Research.

This package contains development files of %name.

%package -n lib%name-devel-docs
Summary: Documentation for %name
Group: Development/Documentation
BuildArch: noarch

%description -n lib%name-devel-docs
Z3 is a high-performance theorem prover being developed at Microsoft
Research.

This package contains documentation for %name.

%package -n python-module-%name
Summary: Python bindings of %name
Group: Development/Python
Requires: lib%name = %EVR
%py_provides %name

%description -n python-module-%name
Z3 is a high-performance theorem prover being developed at Microsoft
Research.

This package contains Python bindings of %name.

%if_with python3
%package -n python3-module-%name
Summary: Python bindings of %name
Group: Development/Python3
Requires: lib%name = %EVR
%py3_provides %name

%description -n python3-module-%name
Z3 is a high-performance theorem prover being developed at Microsoft
Research.

This package contains Python bindings of %name.
%endif

%prep
%setup

# fix path to file
sed -i 's|../src/api/python/z3.py|../src/api/python/z3/z3.py|' doc/mk_api_doc.py

%build
python scripts/mk_make.py
sed -i 's|\$(CC)|$(CC) -g %optflags_shared|' build/Makefile
sed -i 's|@\$(CXX)|$(CXX) -g %optflags_shared|' build/Makefile
%make_build_ext -C build

pushd doc
python mk_api_doc.py
mv api/html ../api
#doxygen z3code.dox
#mv code/html ../code
popd

%install
sed -i 's|\(%python_sitelibdir_noarch\)|%buildroot\1|' build/Makefile
install -d %buildroot%python_sitelibdir_noarch
%makeinstall_std -C build
rm -f  %buildroot%python_sitelibdir_noarch/lib%name.so
ln -s ../../lib%name.so %buildroot%python_sitelibdir_noarch/

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -d %buildroot%python_sitelibdir
cp -a build/python/%{name} %buildroot%python_sitelibdir/

%if_with python3
cp -a build/python build/python3
find build/python3 -type f -name '*.py' -exec sed -i 's|\t|        |g' '{}' +
find build/python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
install -d %buildroot%python3_sitelibdir
cp -a build/python3/%{name} %buildroot%python3_sitelibdir/
ln -s ../../lib%name.so %buildroot%python3_sitelibdir/
%endif

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
export PYTHONPATH=%buildroot%python_sitelibdir
python -c "import z3; print (z3.get_version_string())"
python build/python/example.py
%if_with python3
export PYTHONPATH=%buildroot%python3_sitelibdir
python3 -c "import z3; print (z3.get_version_string())"
python3 build/python3/example.py
%endif

%files
%doc *.txt RELEASE_NOTES
%_bindir/*

%files -n lib%name
%_libdir/*.so

%files -n lib%name-devel
%_includedir/*

%files -n lib%name-devel-docs
%doc examples api
#doc code

%files -n python-module-%name
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%name
%python3_sitelibdir/*
%endif

%changelog
* Mon Mar 26 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 4.5.0-alt1.1
- (NMU) Rebuilt with python-3.6.4.

* Mon Oct 09 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 4.5.0-alt1
- Updated to upstream version 4.5.0.

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.3.2-alt1.git20141024.1.1
- (AUTO) subst_x86_64.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.3.2-alt1.git20141024.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Tue Mar 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.2-alt1.git20141024
- Initial build for Sisyphus

