%def_without python3

%define oname gts
Name: python-module-%oname
Version: 0.3.1
Release: alt2.svn20090606
Summary: Pythonic binding for the GNU Triangulated Surface (GTS) Library
License: LGPLv2+
Group: Development/Python
Url: http://pygts.sourceforge.net/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel libgts-devel libnumpy-devel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel libnumpy-py3-devel python-tools-2to3
%endif

%add_python_req_skip Blender bpy

%description
PyGTS is a python package used to construct, manipulate, and perform
computations on 3D triangulated surfaces. It is a hand-crafted and
pythonic binding for the GNU Triangulated Surface (GTS) Library.

%package -n python3-module-%oname
Summary: Pythonic binding for the GNU Triangulated Surface (GTS) Library (Python 3)
Group: Development/Python3

%description -n python3-module-%oname
PyGTS is a python package used to construct, manipulate, and perform
computations on 3D triangulated surfaces. It is a hand-crafted and
pythonic binding for the GNU Triangulated Surface (GTS) Library.

%prep
%setup

%if_with python3
rm -rf ../python3
cp -a . ../python3
pushd ../python3
for i in $(find ./ -name '*.py'); do
	2to3 -w $i
done
sed -i 's|numpy\/|numpy-py3/|' setup.py
popd
%endif

%build
%add_optflags -fno-strict-aliasing
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc AUTHORS ChangeLog FAQ README* doc/*
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS ChangeLog FAQ README* doc/*
%python3_sitelibdir/*
%endif

%changelog
* Tue Sep 25 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt2.svn20090606
- Disabled dependency on old blender

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3.1-alt1.svn20090606.1
- Rebuild to remove redundant libpython2.7 dependency

* Mon Dec 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1.svn20090606
- Initial build for Sisyphus

