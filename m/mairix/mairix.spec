Name: mairix
Version: 0.17.1
Release: alt1.qa1

Summary: A maildir indexer and searcher
License: GPL
Group: Networking/Mail
Url: http://www.rc0.org.uk/%name
Source: http://www.rc0.org.uk/%name/%name-%{version}.tar.gz


# Automatically added by buildreq on Thu Jul 14 2005
BuildRequires: flex samba-common tetex-core tetex-latex

%description
mairix is a tool for indexing email messages stored in maildir format folders
and performing fast searches on the resulting index.  The output is a new
maildir folder containing symbolic links to the matched messages.

%prep
%setup -q

%build
./configure --prefix=/usr
%make_build
make docs

%install
%makeinstall
%__install -d %buildroot%_infodir
%__install -p mairix.info %buildroot%_infodir

%files
%_bindir/%name
%_infodir/*.info*
%doc README mairix.txt mairix.html mairix.dvi mairix.pdf dotmairixrc.eg

%changelog
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

