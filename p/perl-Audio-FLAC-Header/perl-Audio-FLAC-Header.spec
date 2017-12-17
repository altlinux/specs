# BEGIN SourceDeps(oneline):
BuildRequires: libflac-devel perl(CPAN.pm) perl(Carp.pm) perl(Config.pm) perl(Cwd.pm) perl(DynaLoader.pm) perl(ExtUtils/MM_Unix.pm) perl(ExtUtils/MakeMaker.pm) perl(ExtUtils/Manifest.pm) perl(File/Basename.pm) perl(File/Find.pm) perl(File/Spec.pm) perl(File/Spec/Functions.pm) perl(FileHandle.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Socket.pm) perl(Test/More.pm) perl(YAML/Tiny.pm) perl(inc/Module/Install.pm)
# END SourceDeps(oneline)
%define module_version 2.4
%define module_name Audio-FLAC-Header
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 2.4
Release: alt1.1.1.1.1
Summary: interface to FLAC header metadata.
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/D/DA/DANIEL/%module_name-%module_version.tar.gz

%description
This module returns a hash containing basic information about a FLAC file,
a representation of the embedded cue sheet if one exists,  as well as tag
information contained in the FLAC file's Vorbis tags.
There is no complete list of tag keys for Vorbis tags, as they can be
defined by the user; the basic set of tags used for FLAC files include:

_ALBUM
_ARTIST
_TITLE
_DATE
_GENRE
_TRACKNUMBER
_COMMENT

The information returned by Audio::FLAC::info is keyed by:

_MINIMUMBLOCKSIZE
_MAXIMUMBLOCKSIZE
_MINIMUMFRAMESIZE
_MAXIMUMFRAMESIZE
_TOTALSAMPLES
_SAMPLERATE
_NUMCHANNELS
_BITSPERSAMPLE
_MD5CHECKSUM

Information stored in the main hash that relates to the file itself or is
calculated from some of the information fields is keyed by:

_trackLengthMinutes      : minutes field of track length
_trackLengthSeconds      : seconds field of track length
_trackLengthFrames       : frames field of track length (base 75)
_trackTotalLengthSeconds : total length of track in fractional seconds
_bitRate                 : average bits per second of file
_fileSize                : file size, in bytes


%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc TODO Changes README
%perl_vendor_archlib/A*
%perl_vendor_autolib/*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 2.4-alt1.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 2.4-alt1.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 2.4-alt1.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 2.4-alt1.1
- rebuild with new perl 5.20.1

* Mon Mar 31 2014 Igor Vlasenko <viy@altlinux.ru> 2.4-alt1
- initial import by package builder

