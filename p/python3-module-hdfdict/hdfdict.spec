%define oname hdfdict

Name: python3-module-%oname
Version: 0.3.1
Release: alt1

Summary: Helps h5py to dump and load python dictionaries
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/hdfdict
# https://github.com/SiggiGue/hdfdict.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-h5py python3-module-numpy
BuildRequires: python3-module-Cython python3-module-yaml

%py3_provides %oname
%py3_requires h5py numpy


%description
If you have a hierarchical data structure of numpy arrays in a
dictionary for example, you can use this tool to save this dictionary
into a h5py File() or Group() and load it again. This tool just maps the
hdf Groups to dict keys and the Datset to dict values. Only types
supported by h5py can be used. The dicitonary-keys need to be strings
until now.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test -v

%files
%doc *.md
%python3_sitelibdir/*


%changelog
* Fri Nov 15 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.3.1-alt1
- Version updated to 0.3.1
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.1-alt1.alpha.git20150227.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.1-alt1.alpha.git20150227.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Aug 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1.alpha.git20150227
- Initial build for Sisyphus

