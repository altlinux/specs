Name: texi2html
Version: 1.78
Release: alt1.1
License: GPL
Packager: Pavlov Konstantin <thresh@altlinux.ru>
Group: Text tools
Summary: A highly customizable texinfo to HTML and other formats translator
Source0: %name-%version.tar.bz2
#Source: http://texi2html.cvshome.org/servlets/ProjectDownloadList
Url: http://www.nongnu.org/texi2html
BuildArch: noarch
Conflicts: tetex-core

%description
The basic purpose of texi2html is to convert Texinfo documents into HTML,
and other formats.  Configuration files written in perl provide fine degree
of control over the final output, allowing most every aspect of the final
output not specified in the Texinfo input file to be specified.

%prep
%setup -q

%build
./configure \
             --prefix=%prefix \
             --exec-prefix=%_exec_prefix \
             --bindir=%_bindir \
             --sbindir=%_sbindir \
             --sysconfdir=%_sysconfdir \
             --datadir=%_datadir \
             --includedir=%_includedir \
             --libdir=%_libdir \
             --libexecdir=%_libexecdir \
             --localstatedir=%_localstatedir \
             --sharedstatedir=%_sharedstatedir \
             --mandir=%_mandir \
             --infodir=%_infodir

%install
%make_install DESTDIR=%buildroot install

%files
%doc AUTHORS NEWS README ChangeLog TODO %name.init
%_bindir/%name
%_datadir/texinfo/html/%name.html
%_mandir/man*/%{name}*
%_infodir/%name.info*
%_datadir/%name

%changelog
* Mon Nov 02 2009 Igor Vlasenko <viy@altlinux.ru> 1.78-alt1.1
- NMU (by repocop): the following fixes applied:
  * obsolete-call-in-post-install-info for texi2html

* Wed Jun 27 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.78-alt1
- 1.78 release.

* Wed May 23 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.76-alt2
- Added Conflicts tag in that release.

* Thu May 17 2007 Pavlov Konstantin <thresh@altlinux.ru> 1.76-alt1
- Initial build for Sisyphus.

* Mon Mar 23 2004 Patrice Dumas <pertusus@free.fr> 0:1.69-0.fdr.1
- Initial build.
