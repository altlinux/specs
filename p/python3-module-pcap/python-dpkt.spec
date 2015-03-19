Version: 1.1.1
Release: alt1.git20141230
Summary: Simplified object-oriented Python extension module for libpcap
Url: http://code.google.com/p/pypcap/
License: BSD
Group: Development/Python3
Name: python3-module-pcap
# https://github.com/hellais/pypcap.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: libpcap-devel
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-Cython python-tools-2to3

%description
PyPcapi is simplified object-oriented Python extension module for
libpcap - the current tcpdump.org version, the legacy version shipping
with some of the BSD operating systems.

%prep
%setup
sed -i 's/dylib/so/' setup.py
%ifarch x86_64
sed -i "s/'lib'/'lib64'/g" setup.py
%endif

sed -i "s/'include', *//" setup.py

rm -f pcap.c
find -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%add_optflags -DHAVE_PCAP_FILE
cython3 pcap.pyx
CFLAGS="%optflags" python3 setup.py config
%python3_build_debug

%install
%python3_install

%check
python3 setup.py test
python3 test.py -v

%files
%doc AUTHORS CHANGES LICENSE README test*
%python3_sitelibdir/*

%changelog
* Thu Mar 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.git20141230
- Initial build for Sisyphus

