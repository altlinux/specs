Name: prosper
Version: 1.00.4
Release: alt2

Group: Office
Summary: Presentations style for latex
License: GPL
Url: http://prosper.sourceforge.net
Source: %name-%version.tar.gz
BuildArch: noarch

BuildRequires(pre): rpm-build-texmf

%description
M$ Powerpoint--like presentations in latex.

%add_texmf_req_skip latex/gradient

%prep
%setup -n prosper

%install
%define _compress_method skip

mkdir -p $RPM_BUILD_ROOT%_texmfmain/tex/latex/misc/prosper/
mkdir -p $RPM_BUILD_ROOT%_texmfmain/tex/latex/misc/prosper/contrib/img/
mkdir -p $RPM_BUILD_ROOT%_texmfmain/tex/latex/misc/prosper/img/

cp *.sty *.cls  $RPM_BUILD_ROOT%_texmfmain/tex/latex/misc/prosper/
(cd contrib; cp *.sty *.tex $RPM_BUILD_ROOT%_texmfmain/tex/latex/misc/prosper/contrib/)
(cd contrib/img; cp *.ps $RPM_BUILD_ROOT%_texmfmain/tex/latex/misc/prosper/contrib/img/)
(cd img; cp *.ps *.gif $RPM_BUILD_ROOT%_texmfmain/tex/latex/misc/prosper/img)

%files
%_texmfmain/tex/latex/misc/*
%doc INSTALL README AUTHORS ChangeLog FAQ NEWS doc/*.pdf

%changelog
* Thu Oct 08 2009 Grigory Batalov <bga@altlinux.ru> 1.00.4-alt2
- Hardcoded tetex-latex dependence was removed.
- Specfile cleanup.

* Tue Feb 04 2003 Vitaly Lugovsky <vsl@altlinux.ru> 1.00.4-alt1
- initial release
