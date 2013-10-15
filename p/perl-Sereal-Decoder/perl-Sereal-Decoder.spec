# BEGIN SourceDeps(oneline):
BuildRequires: perl(Data/Dumper.pm) perl(ExtUtils/MakeMaker.pm) perl(ExtUtils/ParseXS.pm) perl(File/Find.pm) perl(File/Path.pm) perl(File/Spec.pm) perl(Scalar/Util.pm) perl(Test/LongString.pm) perl(Test/More.pm) perl(XSLoader.pm)
# END SourceDeps(oneline)
%define module_version 0.37
%define module_name Sereal-Decoder
%define _unpackaged_files_terminate_build 1
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 0.37
Release: alt1
Summary: Fast, compact, powerful binary deserialization
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://cpan.org.ua/authors/id/S/SM/SMUELLER/%module_name-%module_version.tar.gz

%description
This library implements a deserializer for an efficient, compact-output,
and feature-rich binary protocol called *Sereal*.
Its sister module the Sereal::Encoder manpage implements an encoder for this format.
The two are released separately to allow for independent and safer upgrading.

The Sereal protocol version that is compatible with this decoder implementation
is currently protocol version 1. As it stands, it will refuse to attempt to
decode future versions of the protocol, but there is likely going to be an
option to decode the parts of the input that are compatible with version 1
of the protocol. The protocol was designed to allow for this.

The protocol specification and many other bits of documentation
can be found in the github repository. Right now, the specification is at
https://github.com/Sereal/Sereal/blob/master/sereal_spec.pod,
there is a discussion of the design objectives in
https://github.com/Sereal/Sereal/blob/master/README.pod, and the output
of our benchmarks can be seen at
https://github.com/Sereal/Sereal/wiki/Sereal-Comparison-Graphs.


%prep
%setup -n %module_name-%module_version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_archlib/S*
%perl_vendor_autolib/*

%changelog
* Wed Oct 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.37-alt1
- build for Sisyphus (required for perl update)

