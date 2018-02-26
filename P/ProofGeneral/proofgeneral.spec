Name: ProofGeneral
Version: 3.7.1
Release: alt1

Group: Sciences/Mathematics
Summary: Emacs interface for Proof Assistants
License: LFCS, University of Edinburgh
Url: http://proofgeneral.inf.ed.ac.uk/
Source:  ProofGeneral-%version.tgz
Patch: ProofGeneral-3.3-perl.patch
BuildArch: noarch
Requires: perl
AutoReqProv: no
Packager: Ilya Mashkin <oddity@altlinux.ru>

%description

 Proof General is a generic Emacs interface for proof assistants,
 suitable for use by pacifists and Emacs militants alike.
 It is supplied ready-customized for LEGO, Coq, and Isabelle.

%prep
%setup
#%patch0 -p1

%build

%install
%define _compress_method skip

mkdir -p $RPM_BUILD_ROOT/etc/emacs/site-start.d/
mkdir -p $RPM_BUILD_ROOT/usr/share/emacs/site-lisp/proofgeneral/

cat <<EOF >$RPM_BUILD_ROOT/etc/emacs/site-start.d/proofgeneral.el
(load-file "/usr/share/emacs/site-lisp/proofgeneral/generic/proof-site.el")
EOF

tar -cf - . | (cd $RPM_BUILD_ROOT/usr/share/emacs/site-lisp/proofgeneral; tar -xf -)

%files
/etc/emacs/site-start.d/proofgeneral.el
/usr/share/emacs/site-lisp/proofgeneral/*

%doc AUTHORS FAQ CHANGES COPYING BUGS README

%changelog
* Wed Oct 22 2008 Ilya Mashkin <oddity@altlinux.ru> 3.7.1-alt1
- 3.7.1
- fix url

* Thu Oct 24 2002 Vitaly Lugovsky <vsl@altlinux.ru> 3.4-alt1
- new version

* Wed Jun 26 2002 Vitaly Lugovsky <vsl@altlinux.ru> 3.3-alt2
- paths fixed

* Tue Jun 25 2002 Vitaly Lugovsky <vsl@altlinux.ru>
- First RPM release

