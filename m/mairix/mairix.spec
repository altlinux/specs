Name: mairix
Version: 0.24
Release: alt1

Summary: A maildir indexer and searcher

License: GPL
Group: Networking/Mail
Url: http://www.rpcurnow.force9.co.uk/mairix/

Source: %name-%version.tar.gz

# Automatically added by buildreq on Thu Jul 14 2005
BuildRequires: flex samba-common texlive-collection-basic texlive-collection-latexrecommended
BuildRequires: openssl-devel zlib-devel bzlib-devel
# explicitly added texinfo for info files
BuildRequires: texinfo

%description
mairix is a tool for indexing email messages stored in maildir format folders
and performing fast searches on the resulting index.  The output is a new
maildir folder containing symbolic links to the matched messages.

%prep
%setup

%build
./configure --prefix=/usr \
            --mandir=%_mandir

%make_build
#make docs

%install
%makeinstall_std

%files
%doc README
%_bindir/%name
%_man1dir/*
%_man5dir/*

%changelog
* Wed Dec 12 2018 Grigory Ustinov <grenka@altlinux.org> 0.24-alt1
- Build new version (Closes: #24353).

* Sat Mar 03 2018 Igor Vlasenko <viy@altlinux.ru> 0.17.1-alt1.qa3
- NMU: rebuild with texlive instead of tetex

* Thu Dec 03 2015 Igor Vlasenko <viy@altlinux.ru> 0.17.1-alt1.qa2.1
- NMU: added BR: texinfo

* Wed Apr 17 2013 Dmitry V. Levin (QA) <qa_ldv@altlinux.org> 0.17.1-alt1.qa2
- NMU: rebuilt for debuginfo.

* Thu Nov 19 2009 Repocop Q. A. Robot <repocop@altlinux.org> 0.17.1-alt1.qa1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-install-info for mairix
  * postclean-05-filetriggers for spec file

* Fri Jan 27 2006 Alex Murygin <murygin@altlinux.ru> 0.17.1-alt1
- new version

* Thu Jul 14 2005 Alex Murygin <murygin@altlinux.ru> 0.16.1-alt1
- new version

* Wed Feb 09 2005 Alex Murygin <murygin@altlinux.ru> 0.15.2-alt1
- new version

* Thu Aug 12 2004 Alex Murygin <murygin@altlinux.ru> 0.15-alt1
- Initial revision.

