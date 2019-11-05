%define _unpackaged_files_terminate_build 1
%define oname haversine

Name: python3-module-%oname
Version: 0.4.5
Release: alt2

Summary: Calculate the distance bewteen 2 points on Earth
License: GPLv3
Group: Development/Python3
Url: https://pypi.python.org/pypi/haversine/
# https://github.com/mapado/haversine.git

Source0: https://pypi.python.org/packages/57/b4/3b1f5ca78876ad00cbb2a2bf7bcebfe4751c00ddabc47005b59f33835646/%{oname}-%{version}.tar.gz

BuildRequires(pre): rpm-build-python3

%py3_provides %oname


%description
Calculate the distance (in km or in miles) bewteen two points on Earth,
located by their latitude and longitude.

%prep
%setup -q -n %{oname}-%{version}

SUFF=$(echo %_python3_version%_python3_abiflags |sed 's|\.||')
sed -i "s|libhsine.so|libhsine.cpython-$SUFF.so|" %oname/__init__.py

%build
%python3_build_debug

%install
%python3_install

%if "%_libexecdir" != "%_libdir"
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python3 setup.py build_ext -i
python3 -c "from %oname import %oname"

%files
%doc *.txt
%python3_sitelibdir/*


%changelog
* Tue Nov 05 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.4.5-alt2
- disable python2

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.4.5-alt1
- automated PyPI update

* Tue May 24 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.2-alt1.git20150615.1.1.1
- (AUTO) subst_x86_64.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.2-alt1.git20150615.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.2-alt1.git20150615.1
- NMU: Use buildreq for BR.

* Wed Aug 26 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1.git20150615
- Version 0.4.2

* Tue Feb 10 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20130720
- Initial build for Sisyphus

