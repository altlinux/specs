%define rname   pyxmlsec
%def_disable openssl
%def_enable  gnutls
%def_enable  nss 

Name:           python-module-xmlsec
Version:        0.3.1
Release:        alt1
Summary:        Python bindings for the XML Security Library

License:        GPLv2+
Group:          Development/Python
URL:            http://pyxmlsec.labs.libre-entreprise.org/
Packager:       Andrey Cherepanov <cas@altlinux.org>

Source0:        http://labs.libre-entreprise.org/download.php/430/%{rname}-%{version}.tar.gz

Provides:       pyxmlsec = %version-%release

BuildRequires(pre): rpm-build-python
BuildRequires:  python-devel
BuildRequires:  libxmlsec1-devel
BuildRequires:  libxmlsec1-gnutls-devel
BuildRequires:  libxmlsec1-nss-devel


%description
PyXMLSec is a set of Python bindings for the XML Security Library, a C
library based on LibXML2. The library supports major XML security standards
including, XML Signature, XML Encryption, Canonical XML and Exclusive
Canonical XML.


%prep
%setup -q -n %rname-%version

# A non-UTF8 character
iconv -f iso8859-1 -t utf8 <AUTHORS >AUTHORS.utf8
touch -r AUTHORS AUTHORS.utf8
mv AUTHORS.utf8 AUTHORS

%build
echo %{?_enable_openssl:1}%{?_enable_gnutls:2}%{?_enable_nss:3} | %__python setup.py build 

%install
%python_install


%files
%doc AUTHORS ChangeLog COPYING README TODO
%doc docs/
%doc examples/
%python_sitelibdir/*


%changelog
* Mon May 23 2016 Andrey Cherepanov <cas@altlinux.org> 0.3.1-alt1
- New version

* Wed Oct 17 2012 Andrey Cherepanov <cas@altlinux.org> 0.3.0-alt2
- Add docs and examples

* Tue Oct 16 2012 Andrey Cherepanov <cas@altlinux.org> 0.3.0-alt1
- Innitial build in Sisyphus (ALT #27837)

