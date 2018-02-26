%define dist Image-ExifTool

Name: perl-%dist
Version: 8.95
Release: alt1

Summary: Perl module for manipulating EXIF data
License: Perl
Group: Development/Perl

# Switched to real homepage from "%CPAN %dist" as CPAN page does not track
# every released version
URL: http://owl.phy.queensu.ca/~phil/exiftool
Source: %url/%dist-%version.tar.gz
Patch0: perl-image-exiftools-findreq-alt.patch

BuildArch: noarch

Provides: exiftool

# Automatically added by buildreq on Sun Oct 23 2011 (-bi)
BuildRequires: perl-Digest-SHA perl-IO-Compress perl-devel perl-podlators

%description
ExifTool is a customizable set of Perl modules plus an application script for
reading and writing meta information in image, audio and video files, including
the maker note information of many digital cameras by various manufacturers such
as Canon, Casio, FujiFilm, JVC/Victor, Kodak, Leaf, Minolta/Konica-Minolta,
Nikon, Olympus/Epson, Panasonic/Leica, Pentax/Asahi, Ricoh, Sanyo, Sigma/Foveon
and Sony.

%prep
%setup -n %dist-%version
%patch0 -p1

%build
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc Changes README *.args *.fmt ExifTool_config html/*
%_bindir/exiftool
%perl_vendor_privlib/File/
%perl_vendor_privlib/Image/
%_man1dir/exiftool*

%changelog
* Sat Jun 16 2012 Victor Forsiuk <force@altlinux.org> 8.95-alt1
- 8.95

* Tue May 15 2012 Victor Forsiuk <force@altlinux.org> 8.92-alt1
- 8.92

* Sun Apr 15 2012 Victor Forsiuk <force@altlinux.org> 8.87-alt1
- 8.87

* Sun Apr 01 2012 Victor Forsiuk <force@altlinux.org> 8.85-alt1
- 8.85

* Sat Mar 17 2012 Victor Forsiuk <force@altlinux.org> 8.83-alt1
- 8.83

* Sat Mar 03 2012 Victor Forsiuk <force@altlinux.org> 8.80-alt1
- 8.80

* Sun Jan 08 2012 Victor Forsiuk <force@altlinux.org> 8.75-alt1
- 8.75

* Mon Jan 02 2012 Victor Forsiuk <force@altlinux.org> 8.74-alt1
- 8.74

* Sun Nov 27 2011 Victor Forsiuk <force@altlinux.org> 8.71-alt1
- 8.71

* Sun Oct 23 2011 Victor Forsiuk <force@altlinux.org> 8.68-alt1
- 8.68

* Sun Oct 09 2011 Victor Forsiuk <force@altlinux.org> 8.66-alt1
- 8.66

* Sun Sep 25 2011 Igor Vlasenko <viy@altlinux.ru> 8.65-alt1
- automated CPAN update

* Sun Aug 28 2011 Victor Forsiuk <force@altlinux.org> 8.63-alt1
- 8.63

* Sun Jul 17 2011 Victor Forsiuk <force@altlinux.org> 8.61-alt1
- 8.61

* Sun Jun 26 2011 Victor Forsiuk <force@altlinux.org> 8.60-alt1
- 8.60

* Tue Jun 14 2011 Victor Forsiuk <force@altlinux.org> 8.59-alt1
- 8.59

* Mon Apr 25 2011 Victor Forsiuk <force@altlinux.org> 8.56-alt1
- 8.56

* Tue Apr 12 2011 Victor Forsiuk <force@altlinux.org> 8.55-alt1
- 8.55

* Mon Apr 04 2011 Victor Forsiuk <force@altlinux.org> 8.54-alt1
- 8.54

* Mon Mar 28 2011 Victor Forsiuk <force@altlinux.org> 8.53-alt1
- 8.53

* Mon Mar 14 2011 Victor Forsiuk <force@altlinux.org> 8.51-alt1
- 8.51

* Fri Mar 04 2011 Victor Forsiuk <force@altlinux.org> 8.50-alt1
- 8.50

* Mon Feb 07 2011 Victor Forsiuk <force@altlinux.org> 8.48-alt1
- 8.48

* Tue Jan 25 2011 Victor Forsiuk <force@altlinux.org> 8.46-alt1
- 8.46

* Mon Jan 17 2011 Victor Forsiuk <force@altlinux.org> 8.45-alt1
- 8.45

* Fri Jan 14 2011 Victor Forsiuk <force@altlinux.org> 8.43-alt1
- 8.43

* Mon Dec 13 2010 Victor Forsiuk <force@altlinux.org> 8.42-alt1
- 8.42

* Mon Nov 15 2010 Victor Forsiuk <force@altlinux.org> 8.39-alt1
- 8.39

* Mon Oct 11 2010 Victor Forsiuk <force@altlinux.org> 8.34-alt1
- 8.34

* Thu Sep 09 2010 Victor Forsiuk <force@altlinux.org> 8.29-alt1
- 8.29

* Mon Aug 09 2010 Victor Forsiuk <force@altlinux.org> 8.27-alt1
- 8.27

* Thu Jul 01 2010 Victor Forsiuk <force@altlinux.org> 8.24-alt1
- 8.24

* Thu May 20 2010 Victor Forsiuk <force@altlinux.org> 8.19-alt1
- 8.19

* Fri Mar 19 2010 Victor Forsiuk <force@altlinux.org> 8.15-alt1
- 8.15

* Sun Mar 07 2010 Victor Forsiuk <force@altlinux.org> 8.13-alt1
- 8.13

* Fri Feb 12 2010 Victor Forsiuk <force@altlinux.org> 8.10-alt1
- 8.10

* Tue Jan 26 2010 Victor Forsyuk <force@altlinux.org> 8.08-alt1
- 8.08

* Thu Jan 14 2010 Victor Forsyuk <force@altlinux.org> 8.06-alt1
- 8.06

* Fri Dec 11 2009 Victor Forsyuk <force@altlinux.org> 8.01-alt1
- 8.01

* Tue Dec 01 2009 Victor Forsyuk <force@altlinux.org> 8.00-alt1
- 8.00

* Mon Sep 28 2009 Victor Forsyuk <force@altlinux.org> 7.95-alt1
- 7.95

* Tue Sep 08 2009 Victor Forsyuk <force@altlinux.org> 7.93-alt1
- 7.93

* Thu Sep 03 2009 Victor Forsyuk <force@altlinux.org> 7.92-alt1
- 7.92

* Tue Aug 04 2009 Victor Forsyuk <force@altlinux.org> 7.86-alt1
- 7.86

* Wed Jul 01 2009 Victor Forsyuk <force@altlinux.org> 7.81-alt1
- 7.81

* Tue Mar 10 2009 Victor Forsyuk <force@altlinux.org> 7.70-alt1
- 7.70

* Mon Jan 19 2009 Victor Forsyuk <force@altlinux.org> 7.62-alt1
- 7.62

* Mon Dec 29 2008 Victor Forsyuk <force@altlinux.org> 7.59-alt1
- 7.59

* Thu Dec 04 2008 Victor Forsyuk <force@altlinux.org> 7.56-alt1
- 7.56

* Wed Nov 05 2008 Victor Forsyuk <force@altlinux.org> 7.52-alt1
- 7.52

* Thu Oct 23 2008 Victor Forsyuk <force@altlinux.org> 7.49-alt1
- 7.49

* Thu Sep 18 2008 Victor Forsyuk <force@altlinux.org> 7.43-alt1
- 7.43

* Thu Aug 28 2008 Victor Forsyuk <force@altlinux.org> 7.41-alt1
- 7.41

* Fri Aug 01 2008 Victor Forsyuk <force@altlinux.org> 7.39-alt1
- 7.39

* Wed Jun 18 2008 Victor Forsyuk <force@altlinux.org> 7.32-alt1
- 7.32

* Wed Jun 04 2008 Victor Forsyuk <force@altlinux.org> 7.30-alt1
- 7.30

* Thu May 22 2008 Victor Forsyuk <force@altlinux.org> 7.26-alt1
- 7.26

* Wed Apr 30 2008 Victor Forsyuk <force@altlinux.org> 7.25-alt1
- 7.25

* Mon Mar 31 2008 Victor Forsyuk <force@altlinux.org> 7.23-alt1
- 7.23

* Thu Mar 27 2008 Victor Forsyuk <force@altlinux.org> 7.22-alt1
- 7.22

* Thu Mar 13 2008 Victor Forsyuk <force@altlinux.org> 7.21-alt1
- 7.21

* Tue Mar 04 2008 Victor Forsyuk <force@altlinux.org> 7.19-alt1
- 7.19

* Mon Jan 14 2008 Victor Forsyuk <force@altlinux.org> 7.11-alt1
- 7.11

* Fri Dec 28 2007 Victor Forsyuk <force@altlinux.org> 7.08-alt1
- 7.08

* Wed Dec 12 2007 Victor Forsyuk <force@altlinux.org> 7.06-alt1
- 7.06

* Mon Nov 26 2007 Victor Forsyuk <force@altlinux.org> 7.03-alt1
- 7.03

* Wed Oct 24 2007 Victor Forsyuk <force@altlinux.org> 7.00-alt1
- 7.00

* Tue Oct 16 2007 Victor Forsyuk <force@altlinux.org> 6.99-alt1
- 6.99

* Mon Sep 17 2007 Victor Forsyuk <force@altlinux.org> 6.97-alt1
- 6.97

* Fri Sep 07 2007 Victor Forsyuk <force@altlinux.org> 6.96-alt1
- 6.96

* Thu Aug 23 2007 Victor Forsyuk <force@altlinux.org> 6.95-alt1
- 6.95

* Mon Jul 09 2007 Victor Forsyuk <force@altlinux.org> 6.93-alt1
- 6.93

* Thu May 24 2007 Victor Forsyuk <force@altlinux.org> 6.90-alt1
- 6.90

* Tue Apr 24 2007 Victor Forsyuk <force@altlinux.org> 6.86-alt1
- 6.86

* Thu Mar 22 2007 Victor Forsyuk <force@altlinux.org> 6.82-alt1
- 6.82

* Thu Jan 18 2007 Victor Forsyuk <force@altlinux.org> 6.69-alt1
- 6.69

* Mon Dec 11 2006 Victor Forsyuk <force@altlinux.org> 6.64-alt1
- 6.64
- Refresh buildreqs.
- Add sample user configuration file (ExifTool_config) to docs.
- Package (as docs) xmp2iptc.args and iptc2xmp.args.

* Mon Dec 05 2005 Stanislav Yadykin <tosick@altlinux.ru> 5.77-alt1
- 5.77

* Thu Aug 25 2005 Stanislav Yadykin <tosick@altlinux.ru> 5.55-alt1
- 5.55

* Tue Aug 16 2005 Stanislav Yadykin <tosick@altlinux.ru> 5.46-alt1
- 5.46

* Thu Jun 16 2005 Stanislav Yadykin <tosick@altlinux.ru> 5.32-alt1
- 5.38

* Wed May 18 2005 Stanislav Yadykin <tosick@altlinux.ru> 5.18-alt1
- build 5.18 for Sisyphus
