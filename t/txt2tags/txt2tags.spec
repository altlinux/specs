Packager: Alex Negulescu <alecs@altlinux.org>
Summary: Converts text files to HTML, XHTML, sgml, LaTeX, man...
Name: txt2tags
Version: 2.6
Release: alt1.1
License: GPL
Group: Text tools
URL: http://txt2tags.sourceforge.net/
Source: http://dl.sf.net/txt2tags/txt2tags-%{version}.tgz
BuildArch: noarch
BuildRequires: gettext-devel
Requires: python

%description
Txt2tags is a generic text converter. From a simple text file with minimal
markup, it generates documents on the following formats: HTML, XHTML, sgml,
LaTeX, Lout, man, Magic Point (mgp), MoinMoin and Adobe PageMaker. Supports
heading, font beautifiers, verbatim, quote, link, lists, table and image.
There are GUI, Web and cmdline interfaces. It's a single Python script and
no external commands or libraries are needed.

%prep
%setup
for file in $(ls -1 po/*.po); do
	msgfmt -o ${file//.po/.mo} $file
done

%install
%__rm -rf %buildroot
%__install -Dp -m0755 txt2tags %buildroot%_bindir/txt2tags

# manpages
%__install -Dp -m0644 doc/manpage.man %buildroot%_mandir/man1/txt2tags.1
for file in $(ls -1 doc/manpage-*.man); do
	lang=${file##doc/manpage-}
	lang=${lang%%.man}
	%__install -Dp -m0644 $file %buildroot%_mandir/$lang/man1/txt2tags.1
done

# locale files
for file in $(ls -1 po/*.mo); do
	basename=${file##po/}
	lang=${basename%%.mo}
	%__install -Dp -m0644 $file %buildroot%_datadir/locale/$lang/LC_MESSAGES/txt2tags.mo
done

%find_lang %name

# There is a file in the package with a name starting with <tt>._</tt>,
# the file name pattern used by Mac OS X to store resource forks in non-native
# file systems. Such files are generally useless in packages and were usually
# accidentally included by copying complete directories from the source tarball.
find $RPM_BUILD_ROOT -name '._*' -size 1 -print0 | xargs -0 grep -lZ 'Mac OS X' -- | xargs -0 rm -f
# for ones installed as %%doc
find . -name '._*' -size 1 -print0 | xargs -0 grep -lZ 'Mac OS X' -- | xargs -0 rm -f

%clean
%__rm -rf %buildroot

%files
%defattr(-, root, root, 0755)
%doc ChangeLog COPYING README doc/*.pdf extras/ samples/
%_datadir/man/man1/txt2tags.1*
%_datadir/man/*/man1/txt2tags.1*
%_bindir/*

%changelog
* Sat Oct 22 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.6-alt1.1
- Rebuild with Python-2.7

* Wed Jan 12 2011 Alex Negulescu <alecs@altlinux.org> 2.6-alt1
- version up

* Thu Feb 04 2010 Repocop Q. A. Robot <repocop@altlinux.org> 2.5-alt1.1.qa1
- NMU (by repocop): the following fixes applied:
  * macos-resource-fork-file-in-package for txt2tags
  * postclean-05-filetriggers for spec file

* Thu Dec 03 2009 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.5-alt1.1
- Rebuilt with python 2.6

* Mon Nov 09 2009 Alex Negulescu <alecs@altlinux.org> 2.5-alt1
- Initial package
