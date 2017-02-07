Name:           latexmk
Version:        4.52c
Release:        alt1
Summary:        A make-like utility for LaTeX files
Group:          Publishing

%global upstreamver %(sed 's/\\.//' <<< %{version})

License:        %gpl2plus
URL:            http://users.phys.psu.edu/~collins/software/latexmk-jcc/
Source0:        http://users.phys.psu.edu/~collins/software/latexmk-jcc/%{name}-%{upstreamver}.zip
Source1:        latexmk.conf
Source2:        latexmk-README.fedora
# Change the system-wide configuration file to /etc/latexmk.conf and fix the
# man page accordingly.  This patch has not been submitted upstream, as
# upstream needs to be backwards compatible with previous versions of latexmk.
# Fedora has only ever used /etc/latexmk.conf.
Patch0:         latexmk-conf.patch
BuildArch:      noarch
BuildRequires:  rpm-build-perl rpm-build-licenses unzip

Requires:       texlive-latex-base, ghostscript, xdg-utils

%description
Latexmk is a perl script for running LaTeX the correct number of times to
resolve cross references, etc.; it also runs auxiliary programs (bibtex,
makeindex if necessary, and dvips and/or a previewer as requested).  It has
a number of other useful capabilities, for example to start a previewer and
then run latex whenever the source files are updated, so that the previewer
gives an up-to-date view of the document.  The script runs on both UNIX and
MS-WINDOWS (95, ME, XP, etc).  This script is a corrected and improved
version of the original version of latexmk.

Before using a previewer, read the file README.fedora.

%prep
%setup -q -n %name
%patch0

fixtimestamp() {
  touch -r $1.orig $1
  rm -f $1.orig
}

# Fix encoding
pushd example_rcfiles
mv texinfo-latexmkrc texinfo-latexmkrc.orig
iconv -f iso8859-1 -t utf-8 texinfo-latexmkrc.orig > texinfo-latexmkrc
fixtimestamp texinfo-latexmkrc
popd

# Invoke perl directly
sed -i.orig "s|^#\!/usr/bin/env perl|#\!/usr/bin/perl -w|" latexmk.pl
fixtimestamp latexmk.pl

%build
cp -p %SOURCE2 README.fedora

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_man1dir
mkdir -p %buildroot%_sysconfdir
install -m 0755 -p latexmk.pl %buildroot%_bindir/latexmk
install -m 0644 -p latexmk.1 %buildroot%_mandir/man1
install -m 0644 -p %SOURCE1 %buildroot%_sysconfdir

# Remove files we don't want in the docs
rm -f extra-scripts/*.bat

%files
%_bindir/*
%_mandir/man1/*
%config(noreplace) %{_sysconfdir}/latexmk.conf
%doc CHANGES INSTALL README README.fedora extra-scripts example_rcfiles
%doc latexmk.pdf

%changelog
* Tue Feb 07 2017 Evgeny Sinelnikov <sin@altlinux.ru> 4.52c-alt1
- Build for Sisyphus

* Tue Jan 24 2017 Jerry James <loganjerry@gmail.com> - 4.52c-1
- Update to 4.52c

* Sat Jan 14 2017 Jerry James <loganjerry@gmail.com> - 4.51-1
- Update to 4.51

* Tue Oct 25 2016 Jerry James <loganjerry@gmail.com> - 4.48-1
- Update to 4.48

* Thu Apr 28 2016 Jerry James <loganjerry@gmail.com> - 4.45-1
- Update to 4.45

* Thu Feb 25 2016 Jerry James <loganjerry@gmail.com> - 4.44-1
- Update to 4.44

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 4.43a-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Thu Nov 26 2015 Jerry James <jamesjer@diannao.jamezone.org> - 4.43a-1
- Update to 4.43a:
- Source files in directories with non-ASCII names are not correctly detected
  under MiKTeX
- On cleanup, synctex.gz files are deleted only by -C, not by -c

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.42-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Mon Jan 12 2015 Jerry James <loganjerry@gmail.com> - 4.42-1
- Update to 4.42:
- -c also deletes $deps_file if it is used
- Fix bugs associated with the -cd option
- Add missfont.log and the generated synctex.gz to standard cleaned-up files

* Tue Dec  9 2014 Jerry James <loganjerry@gmail.com> - 4.40h-1
- Fix license handling
- Relax LaTeX Requires slightly
- Update to 4.40h:
- When -jobname option is used, quote it on command line.
- Change maintainer's preferred e-mail.
- Attempt to improve handling of errors from (pdf)latex.
- Fix up for the making of -eps-converted-to.pdf
- Improve listing of warning lines from log file.
- Fix failure when using both -cd and -output-directory
- If user's home directory can't be determined, then don't read ~/.latexmkrc
- Introduce configuration variable $silence_logfile_warnings
- In setting $pscmd, allow for non-existent environment variable USER
- Miscellaneous corrections.

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.40-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Mon Jan 27 2014 Jerry James <loganjerry@gmail.com> - 4.40-1
- Update to 4.40:
- Fix failure to clean up correctly when root filename contains '['.

* Mon Dec  2 2013 Jerry James <loganjerry@gmail.com> - 4.39-1
- Update to 4.39:
- Automatic creation of subdirectories of auxdir
- Add error diagnostics to if_source
- Allow print_type = 'auto'
- Fix use of directories with names containing perl glob characters
- Ensure that subdirectories are created properly
- In output of dependencies, include pathname of target file(s) in the rule.
- In -pvc mode, writing of deps file is per make not per overall run.

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.37-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Jul  9 2013 Jerry James <loganjerry@gmail.com> - 4.37-1
- Update URLs
- Update to 4.37:
- Fix failure when current dir's name contains special regexp characters
- Make -rules work with -pvc
- Add -lualatex option
- Allow $clean_ext and $clean_full_ext to contain wildcards
- Fix bug when using revtex4-1.cls

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.35-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Mon Nov 19 2012 Jerry James <loganjerry@gmail.com> - 4.35-1
- Update to 4.35 (fix retaining old dependency info with -gg)

* Wed Oct 24 2012 Jerry James <loganjerry@gmail.com> - 4.34-1
- Update to 4.34 (eliminate unnecessary runs of latex/pdflatex)

* Mon Aug 20 2012 Jerry James <loganjerry@gmail.com> - 4.33c-1
- Update to 4.33c (improved error handling for latex/pdflatex)

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.31-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Mon Apr  2 2012 Jerry James <loganjerry@gmail.com> - 4.31-1
- Update to 4.31 (numerous new features documented at
  http://www.phys.psu.edu/~collins/software/latexmk-jcc/versions.html)

* Tue Jan 10 2012 Jerry James <loganjerry@gmail.com> - 4.30a-2
- Mass rebuild for Fedora 17

* Mon Dec 12 2011 Jerry James <loganjerry@gmail.com> - 4.30a-1
- Add latexmk.pdf to docs
- Update to 4.30a:
- Fix use of bibtex when $aux_dir and/or $out_dir are set
- Documentation of $search_path separator variable
- Work with feynmp package and mpost
- Let dvips find files in the output directory
- In search for cus-deps that can make a missing file, look in $out_dir
- Parse biber 0.9.7 error messages

* Mon Nov 28 2011 Jerry James <loganjerry@gmail.com> - 4.28a-1
- Update to 4.28a:
- Corrects handling of missing files needed by bibtex or biber
- Corrects duplicate invocations of dvipdf and ps2pdf

* Mon Oct 17 2011 Jerry James <loganjerry@gmail.com> - 4.27a-1
- Update to 4.27a:
- Fixes making ps/pdf files via a temporary file with no %%D placeholder
- Adds png to list of graphics extensions for pdflatex
- Adds -norc option to prevent auto-reading of rc files
- Adds -aux-directory and -output-directory options

* Mon Aug 15 2011 Jerry James <loganjerry@gmail.com> - 4.26-1
- Update to 4.26 (fix some bugs in error reporting)

* Mon Jul 11 2011 Jerry James <loganjerry@gmail.com> - 4.25-1
- Update to 4.25 (add deps output file to dependency information)

* Tue Apr 19 2011 Jerry Jamse <loganjerry@gmail.com> - 4.23a-1
- Update to 4.23a (fix detection of source files listed in .fls file)

* Mon Mar 28 2011 Jerry James <loganjerry@gmail.com> - 4.23-1
- Update to 4.23 (several bug fixes, new dependency-tracking functionality)
- Drop BuildRoot and %%clean

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.22e-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb  7 2011 Jerry James <loganjerry@gmail.com> - 4.22e-1
- Update to 4.22e (fixes incorrect error handling when reading init files)

* Mon Jan  3 2011 Jerry James <loganjerry@gmail.com> - 4.22-1
- Update to 4.22 (fixes more parse problems, adds biber support)

* Mon Aug  2 2010 Jerry James <loganjerry@gmail.com> - 4.18-1
- Update to 4.18 (parses natbib's citation-undefined warning)
- Drop latexmk-man.patch, upstreamed.

* Tue Jul  6 2010 Jerry James <loganjerry@gmail.com> - 4.17-1
- Update to 4.17 (fixes log file misparse with filename-space-message sequence)
- Add latexmk-man.patch to fix insufficiently escaped man page constructs.

* Mon May 24 2010 Jerry James <loganjerry@gmail.com> - 4.16a-1
- Update to 4.16a (solves problem with preview files on NFS filesystems)

* Mon May 17 2010 Jerry James <loganjerry@gmail.com> - 4.16-1
- Update to 4.16 (solves problem with misparsed log files)

* Wed Apr 21 2010 Jerry James <loganjerry@gmail.com> - 4.15c-1
- Update to 4.15c (solves failure to detect some dependent files)

* Mon Apr 12 2010 Jerry James <loganjerry@gmail.com> - 4.15-1
- Update to 4.15 (some diagnostic and error-handling improvements)

* Mon Jan 25 2010 Jerry James <loganjerry@gmail.com> - 4.13a-1
- Update to 4.13a (fixes bug with -C not deleting files).

* Mon Jan 18 2010 Jerry James <loganjerry@gmail.com> - 4.13-1
- Update to 4.13.

* Tue Dec 29 2009 Jerry James <loganjerry@gmail.com> - 4.12-1
- Update to 4.12 to get new option to not run bibtex.
- Add a missing semicolon to the conf file (bz 551082).

* Tue Dec  1 2009 Jerry James <loganjerry@gmail.com> - 4.11-1
- Update to 4.11.

* Mon Aug 24 2009 Jerry James <loganjerry@gmail.com> - 4.10-1
- Update to 4.10 to correctly handle files produced by epstopdf.

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.07-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Jun  1 2009 Jerry James <loganjerry@gmail.com> - 4.07-1
- Update to 4.07 to correct problem with exiting from preview-continuous mode.

* Mon Apr 13 2009 Jerry James <loganjerry@gmail.com> - 4.05-1
- Update to 4.05 to correct problems when running latex and pdflatex on the
  same source file.

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.03-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan  6 2009 Jerry James <loganjerry@gmail.com> - 4.03-1
- Update to 4.03 to fix log file parsing

* Mon Dec  1 2008 Jerry James <loganjerry@gmail.com> - 4.02b-1
- Update to 4.02b to fix bz 473430

* Mon Oct 13 2008 Jerry James <loganjerry@gmail.com> - 4.01-1
- New version 4.01.

* Wed Sep 24 2008 Jerry James <loganjerry@gmail.com> - 4.00e-1
- New version 4.00e.
- Drop the perl patch; the script finds it just fine

* Fri Aug 31 2007 Jerry James <loganjerry@gmail.com> - 3.20-1
- New version 3.20.
- Texlive isn't as near as I thought; require the tetex packages for now.

* Tue Aug 21 2007 Jerry James <loganjerry@gmail.com> - 3.08n-5
- Update license tag

* Tue Mar 27 2007 Jerry James <Jerry.James@usu.edu> - 3.08n-4
- Avoid tetex vs. texlive issues by Requiring the binaries.

* Tue Mar 20 2007 Jerry James <Jerry.James@usu.edu> - 3.08n-3
- Use xdg-open for the DVI and PostScript previewers also.
- Describe previewer configuration in README.fedora.

* Mon Mar 19 2007 Jerry James <Jerry.James@usu.edu> - 3.08n-2
- Use xdg-open instead of explicitly invoking evince.
- Package the extra-scripts directory as documentation.
- Fix a few other packaging infelicities as pointed out in Extras review.

* Tue Feb 27 2007 Jerry James <Jerry.James@usu.edu> - 3.08n-1
- Initial RPM
