%define _unpackaged_files_terminate_build 1

%define oname pysendfile

Name: python-module-%oname
Version: 2.0.1
Release: alt1
Summary: Python interface to the sendfile(2) system call

License: MIT
Group: Development/Python
Url: https://pypi.org/project/pysendfile/
# Source-git: https://github.com/giampaolo/pysendfile
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%description
sendfile(2) is a system call which provides a "zero-copy" way of copying
data from one file descriptor to another (a socket). The phrase
"zero-copy" refers to the fact that all of the copying of data between
the two descriptors is done entirely by the kernel, with no copying of
data into user-space buffers. This is particularly useful when sending a
file over a socket (e.g. FTP).

%package -n python3-module-%oname
Summary: Python3 interface to the sendfile(2) system call
Group: Development/Python3

%description -n python3-module-%oname
sendfile(2) is a system call which provides a "zero-copy" way of copying
data from one file descriptor to another (a socket). The phrase
"zero-copy" refers to the fact that all of the copying of data between
the two descriptors is done entirely by the kernel, with no copying of
data into user-space buffers. This is particularly useful when sending a
file over a socket (e.g. FTP).

%prep
%setup
rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install

pushd ../python3
%python3_install
popd

%check
PYTHONPATH="%buildroot%python_sitelibdir" python test/test_sendfile.py

pushd ../python3
PYTHONPATH="%buildroot%python3_sitelibdir" python3 test/test_sendfile.py
popd

%files
%doc README.rst LICENSE
%python_sitelibdir/sendfile.so
%python_sitelibdir/pysendfile-*.egg-info/

%files -n python3-module-%oname
%doc README.rst LICENSE
%python3_sitelibdir/sendfile.cpython-*.so
%python3_sitelibdir/pysendfile-*.egg-info/

%changelog
* Sat Jan 12 2019 Stanislav Levin <slev@altlinux.org> 2.0.1-alt1
- 2.0.0 -> 2.0.1.
- Enabled build of Python3 module.

* Thu Sep 13 2012 Pavel Shilovsky <piastry@altlinux.org> 2.0.0-alt1
- Initial release for Sisyphus (based on Fedora)
