Name: ca-certificates
Version: 2017.11.22
Release: alt1

Summary: Common CA Certificates
License: MPL/GPL/LGPL
Group: System/Base
BuildArch: noarch

Source0: mozilla.tar
Source1: alt.tar

BuildRequires: openssl perl-Encode

%description
This package contains a bundle of X.509 certificates of public
Certificate Authorities (CA).  This is useful for any applications to
verify SSL/TLS connection.

Note that certificate authorities whose certificates are included in
this package are not in any way audited for trustworthiness and RFC3647
compliance, and that full responsibility to assess them rests with the
user.

%prep
%setup -c -a1
patch -p1 < mozilla/mk-ca-bundle.patch

%build
export TZ=UTC
pushd mozilla
	./mk-ca-bundle.pl -t crt
popd
pushd alt
	for t in alt; do
		printf '#\n# %%s\n#\n\n' 'ALT CA'
		openssl x509 -sha256 -in $t.crt -text -fingerprint
		printf '\n\n'
	done >crt
popd
cat {mozilla,alt}/crt >ca-bundle.crt

%install
install -pDm644 ca-bundle.crt %buildroot%_datadir/%name/ca-bundle.crt
mkdir -p %{buildroot}%_sysconfdir/pki/tls/certs
ln -s %_datadir/%name/ca-bundle.crt %{buildroot}%_sysconfdir/pki/tls/certs

%files
%dir %_sysconfdir/pki/tls
%dir %_sysconfdir/pki/tls/certs
%_sysconfdir/pki/tls/certs/*
%_datadir/%name

%changelog
* Thu Dec 14 2017 L.A. Kostis <lakostis@altlinux.ru> 2017.11.22-alt1
- mozilla:
    + updated to October 2017 batch of root CA changes.
      (#bmo 1408080).
    + added Certum CA Root certificate back (#bmo 1418678).
- mozilla/mk-ca-bundle.pl: updated to v1.27.
- update BR: added perl-Encode to handle utf8 cert data.

* Mon May 22 2017 L.A. Kostis <lakostis@altlinux.ru> 2017.04.04-alt1
- mozilla: updated to March 2017 batch of root CA changes.
  (#bmo 1350859).

* Fri Sep 30 2016 L.A. Kostis <lakostis@altlinux.ru> 2016.09.28-alt1
- mozilla: updated to September 2016 CA batch root changes.
  (#bmo 1296689).

* Fri Jun 24 2016 L.A. Kostis <lakostis@altlinux.ru> 2016.05.25-alt1
- mozilla: updated to May 2016 CA batch root changes.
  (#bmo 1275533).

* Wed May 04 2016 L.A. Kostis <lakostis@altlinux.ru> 2016.02.25-alt1
- mozilla: updated to February 2016 batch root CA changes.
  (#bmo 1247990).

* Sun Feb 14 2016 L.A. Kostis <lakostis@altlinux.ru> 2015.10.29-alt1
- mozilla: updated to October 2015 batch root CA changes
  (#bmo 1214729).
- added /etc/pki/tls/certs dir (closes: #31213).

* Fri Aug 28 2015 L.A. Kostis <lakostis@altlinux.ru> 2015.08.04-alt1
- mozilla/certdata.txt: updated ca-certificates to v2.5.
- mozilla/mk-ca-bundle.pl:
  + updated to v1.25.
  + use SHA256 for fingerprint.
  + remove MD5 from valid cert signature list.
- remove cacert (untrusted signature).

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
