Name: impose+
Version: 0.2
Release: alt2

Summary: A set of PostScript utilities
Summary(ru_RU.KOI8-R): Набор программ для обработки PostScript

License: GPL
Group: Text tools
Url: http://freshmeat.net/projects/impose/

Packager: Vitaly Lipatov <lav@altlinux.ru>

Source: http://freshmeat.net/redir/impose/4391/url_tgz/%name-%version.tar.bz2

BuildArchitectures: noarch

%description
impose+ is a set of postscript utilities. The main program of impose+
is impose which is used for two-up printing of DSC complient postscript.
This includes postscript from e.g. mozilla, dvips, and FrameMaker. It
makes an effort to remove white space from the printout by probing the
original postscript for the bounding box of the printed area. This makes
the output much more esthetic than does a simplistic layout of non-cropped
original papers.

%prep
%setup

%install
%makeinstall

%files
%doc AUTHORS README TODO html/*
%_bindir/*

%changelog
* Mon Nov 08 2004 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt2
- fix spec

* Sun Jun 13 2004 Vitaly Lipatov <lav@altlinux.ru> 0.2-alt1
- first build for Sisyphus
