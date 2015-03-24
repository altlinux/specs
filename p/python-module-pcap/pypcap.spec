Version: 1.1.1
Release: alt1
Summary: Simplified object-oriented Python extension module for libpcap
Url: https://github.com/hellais/pypcap
License: BSD
Group: Development/Python
%setup_python_module pcap
Name: %packagename
Source: pypcap-%version.tar.gz
Patch: pypcap-1.1.1-setup.patch

# Automatically added by buildreq on Tue Mar 24 2015
# optimized out: alt-gpgkeys alternatives ca-certificates common-licenses control cpio diffstat ed elfutils emacs-base glib2-locales gnu-config less libcap-ng libcloog-isl4 libncurses-devel libtinfo-devel makeinfo openssh-clients openssh-common pam0_mktemp pam0_passwdqc pam0_tcb pam0_userpass perl-threads pkg-config python-base python-devel python-module-Pyrex-pickles python-modules python-modules-bsddb python-modules-compiler python-modules-ctypes python-modules-curses python-modules-email python-modules-encodings python-modules-hotshot python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python-tools-2to3 rsync setarch shadow-convert strace sysvinit-utils tcb-utils termutils tex-common texi2dvi time tzdata vim-common xml-common xxd xz
BuildRequires: libpcap-devel python-module-Pyrex python-module-setuptools

%description
PyPcap is simplified object-oriented Python extension module for libpcap
- the current tcpdump.org version, the legacy version shipping with some
of the BSD operating systems

%prep
%setup -n pypcap-%version
%patch -p1

%build
python setup.py config
%python_build
python setup.py build

%install
%python_install
#python setup.py install --prefix=%prefix --root=$RPM_BUILD_ROOT --record=INSTALLED_FILES

%files
%doc CHANGES LICENSE README test*
%python_sitelibdir/*

%changelog
* Tue Mar 24 2015 Fr. Br. George <george@altlinux.ru> 1.1.1-alt1
- Autobuild version bump to 1.1.1
- Fix build
- Rename module as it provides python2.7(pcap), not pypcap

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1-alt2.1
- Rebuild with Python-2.7

* Thu Aug 26 2010 Fr. Br. George <george@altlinux.ru> 1.1-alt2
- Fix build

* Sat Nov 21 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1.1
- Rebuilt with python 2.6

* Sat Jan 10 2009 Fr. Br. George <george@altlinux.ru> 1.1-alt1
- Initial build from scratch

