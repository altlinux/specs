%define _unpackaged_files_terminate_build 1
%define oname pysendfile

Name: python3-module-%oname
Version: 2.0.1
Release: alt3

Summary: Python interface to the sendfile(2) system call
License: MIT
Group: Development/Python3

Url: https://pypi.org/project/pysendfile/
# Source-git: https://github.com/giampaolo/pysendfile
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-dev


%description
sendfile(2) is a system call which provides a "zero-copy" way of copying
data from one file descriptor to another (a socket). The phrase
"zero-copy" refers to the fact that all of the copying of data between
the two descriptors is done entirely by the kernel, with no copying of
data into user-space buffers. This is particularly useful when sending a
file over a socket (e.g. FTP).

%prep
%setup

%build
%python3_build

%install
%python3_install

%check
PYTHONPATH="%buildroot%python3_sitelibdir" python3 test/test_sendfile.py

%files
%doc README.rst LICENSE
%python3_sitelibdir/sendfile.cpython-*.so
%python3_sitelibdir/pysendfile-*.egg-info/


%changelog
* Wed Feb 12 2020 Andrey Bychkov <mrdrew@altlinux.org> 2.0.1-alt3
- Build for python2 disabled.

* Sun Apr 07 2019 Michael Shigorin <mike@altlinux.org> 2.0.1-alt2
- added explicit BR: python{,3}-dev to ease e2k python upgrade

* Sat Jan 12 2019 Stanislav Levin <slev@altlinux.org> 2.0.1-alt1
- 2.0.0 -> 2.0.1.
- Enabled build of Python3 module.

* Thu Sep 13 2012 Pavel Shilovsky <piastry@altlinux.org> 2.0.0-alt1
- Initial release for Sisyphus (based on Fedora)
