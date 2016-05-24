# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1.git20141024.1.1
%def_with python3

Name: z3
Version: 4.3.2
#Release: alt1.git20141024.1
Summary: High-performance theorem prover
License: Noncommercial use only
Group: Sciences/Mathematics
Url: http://z3.codeplex.com/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://git01.codeplex.com/z3
Source: %name-%version.tar

BuildRequires(pre): rpm-macros-make
BuildPreReq: python-devel gcc-c++ doxygen graphviz
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python-tools-2to3
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
%makeinstall_std -C build PREFIX=%buildroot%prefix
rm -f  %buildroot%python_sitelibdir_noarch/lib%name.so
ln -s ../../lib%name.so %buildroot%python_sitelibdir_noarch/

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%if_with python3
find build -type f -name '*.py' -exec sed -i 's|\t|        |g' '{}' +
find build -type f -name '*.py' -exec 2to3 -w -n '{}' +
install -d %buildroot%python3_sitelibdir
install -m644 build/%{name}*.py %buildroot%python3_sitelibdir/
ln -s ../../lib%name.so %buildroot%python3_sitelibdir/
%endif

%check
export LD_LIBRARY_PATH=%buildroot%_libdir
export PYTHONPATH=%buildroot%python_sitelibdir
python -c "import z3; print (z3.get_version_string())"
python build/example.py
%if_with python3
export PYTHONPATH=%buildroot%python3_sitelibdir
python3 -c "import z3; print (z3.get_version_string())"
python3 build/example.py
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
* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.3.2-alt1.git20141024.1.1
- (AUTO) subst_x86_64.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.3.2-alt1.git20141024.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Tue Mar 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.3.2-alt1.git20141024
- Initial build for Sisyphus

