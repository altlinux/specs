%define _unpackaged_files_terminate_build 1
%define oname pyprof2calltree

%def_with python3

Name: python-module-%oname
Version: 1.4.0
Release: alt1
Summary: Help visualize profiling data from cProfile with kcachegrind
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/pyprof2calltree/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/ad/d9/2e3380728d3c8709574d81b749020fdc047073576cecba38fe14d6672ce3/%{oname}-%{version}.tar.gz
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%description
Script to help visualize profiling data collected with the cProfile
python module with the kcachegrind (screenshots) graphical calltree
analyser.

This is a rebranding of the venerable
http://www.gnome.org/~johan/lsprofcalltree.py script by David Allouche
et Al. It aims at making it easier to distribute (e.g. through pypi) and
behave more like the scripts of the debian kcachegrind-converters
package. The final goal is to make it part of the official upstream
kdesdk package.

%package -n python3-module-%oname
Summary: Help visualize profiling data from cProfile with kcachegrind
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Script to help visualize profiling data collected with the cProfile
python module with the kcachegrind (screenshots) graphical calltree
analyser.

This is a rebranding of the venerable
http://www.gnome.org/~johan/lsprofcalltree.py script by David Allouche
et Al. It aims at making it easier to distribute (e.g. through pypi) and
behave more like the scripts of the debian kcachegrind-converters
package. The final goal is to make it part of the official upstream
kdesdk package.

%prep
%setup -q -n %{oname}-%{version}

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
pushd %buildroot%_bindir
for i in $(ls); do
	mv $i $i.py3
done
popd
%endif

%python_install

%files
%doc *.txt
%_bindir/*
%if_with python3
%exclude %_bindir/*.py3
%endif
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%_bindir/*.py3
%python3_sitelibdir/*
%endif

%changelog
* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 1.4.0-alt1
- automated PyPI update

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3.2-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Jul 30 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.2-alt2
- Added provides %oname for Python 3

* Tue Jul 15 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.2-alt1
- Version 1.3.2
- Added module for Python 3

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.1-alt1
- Version 1.3.1

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus

