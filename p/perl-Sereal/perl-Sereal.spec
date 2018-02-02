%define _unpackaged_files_terminate_build 1
%define module_name Sereal
Epoch: 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Sereal/Decoder.pm) perl(Sereal/Encoder.pm) perl(Test/More.pm) perl(Test/Deep/NoTest.pm) perl(Test/LongString.pm) perl(Test/Warn.pm)
# END SourceDeps(oneline)
BuildRequires: rpm-build-perl perl-devel perl-podlators

Name: perl-%module_name
Version: 4.005
Release: alt1
Summary: Fast, compact, powerful binary (de-)serialization
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source0: http://www.cpan.org/authors/id/Y/YV/YVES/%{module_name}-%{version}.tar.gz
BuildArch: noarch

%description
*Sereal* is an efficient, compact-output, binary and feature-rich
serialization protocol. The Perl encoder is implemented as the
the Sereal::Encoder manpage module, the Perl decoder correspondingly as 
the Sereal::Decoder manpage. They are distributed separately to allow for
safe upgrading without downtime. (Hint: Upgrade the decoder everywhere
first, then the encoder.)

This `Sereal' module is a very thin wrapper around both `Sereal::Encoder'
and `Sereal::Decoder'. It depends on both and loads both. So if you have
a user of both encoder and decoder, it is enough to depend on a particular
version of `Sereal' and you'll get the most recent released versions
of `Sereal::Encoder' and `Sereal::Decoder' whose version is smaller than
or equal to the version of `Sereal' you depend on.

The protocol specification and many other bits of documentation
can be found in the github repository. Right now, the specification is at
https://github.com/Sereal/Sereal/blob/master/sereal_spec.pod,
there is a discussion of the design objectives in
https://github.com/Sereal/Sereal/blob/master/README.pod, and the output
of our benchmarks can be seen at
https://github.com/Sereal/Sereal/wiki/Sereal-Comparison-Graphs.


%prep
%setup -q -n %{module_name}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/S*

%changelog
* Thu Feb 01 2018 Igor Vlasenko <viy@altlinux.ru> 1:4.005-alt1
- automated CPAN update

* Wed Dec 20 2017 Igor Vlasenko <viy@altlinux.ru> 1:4.004-alt1
- automated CPAN update

* Tue Sep 20 2016 Igor Vlasenko <viy@altlinux.ru> 1:3.015-alt1
- automated CPAN update

* Mon Dec 07 2015 Igor Vlasenko <viy@altlinux.ru> 1:3.014-alt1
- automated CPAN update

* Sat Nov 28 2015 Igor Vlasenko <viy@altlinux.ru> 1:3.008-alt1
- automated CPAN update

* Fri Nov 27 2015 Igor Vlasenko <viy@altlinux.ru> 1:3.007-alt1
- automated CPAN update

* Mon Nov 16 2015 Igor Vlasenko <viy@altlinux.ru> 1:3.006-alt1
- automated CPAN update

* Wed Nov 11 2015 Igor Vlasenko <viy@altlinux.ru> 1:3.005-alt2
- moved to Sisyphus

* Mon Jan 19 2015 Igor Vlasenko <viy@altlinux.ru> 1:3.005-alt1
- regenerated from template by package builder

* Mon Jan 05 2015 Igor Vlasenko <viy@altlinux.ru> 1:3.004-alt1
- regenerated from template by package builder

* Wed Oct 22 2014 Igor Vlasenko <viy@altlinux.ru> 1:3.003-alt1
- regenerated from template by package builder

* Fri Sep 05 2014 Igor Vlasenko <viy@altlinux.ru> 1:3.002-alt1
- regenerated from template by package builder

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 1:3.001-alt1
- regenerated from template by package builder

* Tue Apr 15 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.11-alt2
- regenerated from template by package builder

* Tue Apr 01 2014 Igor Vlasenko <viy@altlinux.ru> 2.060-alt1
- regenerated from template by package builder

* Sat Jan 11 2014 Igor Vlasenko <viy@altlinux.ru> 2.030-alt1
- regenerated from template by package builder

* Mon Jan 06 2014 Igor Vlasenko <viy@altlinux.ru> 2.011-alt1
- regenerated from template by package builder

* Thu Oct 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.370-alt1
- initial import by package builder

