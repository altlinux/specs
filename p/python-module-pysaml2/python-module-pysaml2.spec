%define sname pysaml2
%add_findreq_skiplist %python3_sitelibdir/saml2/s2repoze/plugins/*

Name: python-module-%sname
Version: 4.6.5
Release: alt1
Summary: PySAML2 - SAML2 in Python
License: ASL 2.0

Url: https://idpy.org
Group: Development/Python

Source: https://pypi.python.org/packages/source/p/%sname/%sname-%version.tar.gz

BuildArch: noarch

BuildRequires: python-devel
BuildRequires: python-module-setuptools

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel
BuildRequires: python3-module-setuptools

%description
PySAML2 is a pure python implementation of SAML Version 2 Standard.
It contains all necessary pieces for building a SAML2 service provider
or an identity provider. The distribution contains examples of both.
Originally written to work in a WSGI environment there are extensions
that allow you to use it with other frameworks.

%package -n python3-module-%sname
Summary: PySAML2 - SAML2 in Python
Group: Development/Python3

%description -n python3-module-%sname
PySAML2 is a pure python implementation of SAML Version 2 Standard.
It contains all necessary pieces for building a SAML2 service provider
or an identity provider. The distribution contains examples of both.
Originally written to work in a WSGI environment there are extensions
that allow you to use it with other frameworks.

%prep
%setup -n %sname-%version

sed -i '/argparse/d' setup.py

# Avoid non-executable-script rpmlint while maintaining timestamps
find src -name \*.py |
while read source; do
  if head -n1 "$source" | grep -F '/usr/bin/env'; then
    touch --ref="$source" "$source".ts
    sed -i '/\/usr\/bin\/env python/{d;q}' "$source"
    touch --ref="$source".ts "$source"
    rm "$source".ts
  fi
done
# special case for parse_xsd generated file which have lines like:
#!!!! 'NoneType' object has no attribute 'py_class'
source="src/saml2/schema/wsdl.py"
touch --ref="$source" "$source".ts
sed -i '1,3{d;q}' "$source"
touch --ref="$source".ts "$source"
rm "$source".ts

rm -rf ../python3
cp -a . ../python3

%build
%python_build

pushd ../python3
%python3_build
popd

%install
%python_install
mv %buildroot%_bindir/make_metadata.py %buildroot%_bindir/make_metadata.py2
mv %buildroot%_bindir/mdexport.py %buildroot%_bindir/mdexport.py2
mv %buildroot%_bindir/merge_metadata.py %buildroot%_bindir/merge_metadata.py2
mv %buildroot%_bindir/parse_xsd2.py %buildroot%_bindir/parse_xsd2.py2

pushd ../python3
%python3_install
popd

%files
%doc README.rst
%_bindir/*.py2
%python_sitelibdir/*

%files -n python3-module-%sname
%doc README.rst
%_bindir/*.py
%python3_sitelibdir/*

%changelog
* Wed Dec 19 2018 Alexey Shabalin <shaba@altlinux.org> 4.6.5-alt1
- 4.6.5
- add python3 package

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 3.0.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jun 14 2017 Vitaly Lipatov <lav@altlinux.ru> 3.0.2-alt1
- new version 3.0.2 (with rpmrb script)

* Wed Apr 01 2015 Alexey Shabalin <shaba@altlinux.ru> 2.4.0-alt1
- Initial build


