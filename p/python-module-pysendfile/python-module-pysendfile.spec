Name:		python-module-pysendfile
Version:	2.0.0
Release:	alt1
Summary:	Python interface to the sendfile(2) system call

License:	MIT
Group:		Development/Python
URL:		http://code.google.com/p/pysendfile/
Source0:	%{name}-%{version}.tar.gz

BuildRequires: python-devel
BuildRequires: python-module-distribute

%description
sendfile(2) is a system call which provides a "zero-copy" way of copying
data from one file descriptor to another (a socket). The phrase
"zero-copy" refers to the fact that all of the copying of data between
the two descriptors is done entirely by the kernel, with no copying of
data into user-space buffers. This is particularly useful when sending a
file over a socket (e.g. FTP).

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS" %{__python} setup.py build

%install
%{__python} setup.py install -O1 --skip-build --root %buildroot

%check
PYTHONPATH="%buildroot/%{python_sitelibdir}" %{__python} test/test_sendfile.py

%files
%doc README LICENSE
%attr(755, root, root) %{python_sitelibdir}/sendfile.so
%{python_sitelibdir}/*

%changelog
* Thu Sep 13 2012 Pavel Shilovsky <piastry@altlinux.org> 2.0.0-alt1
- Initial release for Sisyphus (based on Fedora)
