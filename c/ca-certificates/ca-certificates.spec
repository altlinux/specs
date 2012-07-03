Name: ca-certificates
Version: 2012.01.17
Release: alt1

Summary: Common CA Certificates
License: MPL/GPL/LGPL
Group: System/Base
BuildArch: noarch

Source0: mozilla.tar
Source1: alt.tar
Source2: cacert.org.tar

BuildRequires: openssl

%description
This package contains a bundle of X.509 certificates of public Certificate
Authorities (CA).  This is useful for any applications to verify SSL/TLS
connection.
Note that certificate authorities whose certificates are included in
this package are not in any way audited for trustworthiness and RFC3647
compliance, and that full responsibility to assess them rests with
the user.

%prep
%setup -c -a1 -a2
patch -p0 < mozilla/mk-ca-bundle.patch

%build
export TZ=UTC
pushd mozilla
	./mk-ca-bundle.pl -t crt
popd
pushd alt
	for t in alt; do
		printf '#\n# %%s\n#\n\n' 'ALT CA'
		openssl x509 -in $t.crt -text -fingerprint
		printf '\n\n'
	done >crt
popd
pushd cacert.org
	for t in root class3; do
		printf '#\n# %%s\n#\n\n' "http://www.cacert.org/certs/$t.crt"
		openssl x509 -in "$t.crt" -text -fingerprint
		printf '\n\n'
	done >crt
popd
cat {mozilla,alt,cacert.org}/crt >ca-bundle.crt

%install
install -pDm644 ca-bundle.crt %buildroot%_datadir/%name/ca-bundle.crt

%files
%_datadir/%name

%changelog
* Wed Feb 08 2012 Dmitry V. Levin <ldv@altlinux.org> 2012.01.17-alt1
- mozilla/certdata.txt: updated to revision 1.81.
- Filtered out untrusted certs from mozilla bundle (closes: #26904).

* Thu Nov 10 2011 Dmitry V. Levin <ldv@altlinux.org> 2011.11.03-alt1
- mozilla/certdata.txt: updated to revision 1.80.

* Fri Sep 02 2011 Dmitry V. Levin <ldv@altlinux.org> 2011.09.02-alt1
- mozilla/certdata.txt: updated to revision 1.78.

* Thu Sep 30 2010 Dmitry V. Levin <ldv@altlinux.org> 2010.08.27-alt1
- mozilla/certdata.txt: Updated to revision 1.65.

* Sun Apr 05 2009 Dmitry V. Levin <ldv@altlinux.org> 2009.01.15-alt1
- cacert.org: Added http://www.cacert.org/certs/root.crt (closes: #14119).
- mozilla/certdata.txt: Updated to revision 1.51 (closes: #19484).

* Tue Feb 06 2007 Dmitry V. Levin <ldv@altlinux.org> 2007.02.06-alt1
- Imported a bundle of X.509 certificates of public Certificate
  Authorities (CA) from openssl package to this package.
- Updated Mozilla's root CA list.
- Added ALT Root CA.
- Added cacert.org Root CA.
