BuildRequires: perl-podlators
%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires: perl(File/HomeDir.pm) perl(File/chdir.pm) perl(List/MoreUtils.pm) perl(Moose.pm) perl(Moose/Autobox.pm) perl(Moose/Util/TypeConstraints.pm) perl(MooseX/Types/Path/Class.pm) perl(Path/Class.pm) perl(Pod/Usage.pm) perl(Test/Differences.pm) perl(Test/Exception.pm) perl(YAML/Tiny.pm)
# END SourceDeps(oneline)
%define module_version 0.004
%define module_name File-Corresponding
BuildRequires: rpm-build-perl perl-devel perl-podlators perl(Module/Build.pm)

Name: perl-%module_name
Version: 0.004
Release: alt1
Summary: File::Corresponding - Find corresponding files in the directory tree
Group: Development/Perl
License: perl
Url: %CPAN %module_name

Source: http://www.cpan.org/authors/id/J/JO/JOHANL/File-Corresponding-%{version}.tar.gz
BuildArch: noarch

%description
In a source tree it is common to have files with the same name, but in
different places in the directory tree.

%package scripts
Summary: %name scripts
Group: Development/Perl
Requires: %{?epoch:%epoch:}%name = %version-%release

%description scripts
scripts for %name


%prep
%setup -n %module_name-%module_version
# they say die is ok
rm t/corresponding-config.t
#[ %version == 0.004 ] && rm t/corresponding-group-corresponding.t t/corresponding-corresponding.t t/corresponding-config.t

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_privlib/F*

%files scripts
%_bindir/*
%_man1dir/*

%changelog
* Thu Nov 12 2015 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1
- automated CPAN update

* Tue Jun 03 2014 Igor Vlasenko <viy@altlinux.ru> 0.003-alt3
- fixed build

* Wed Feb 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.003-alt2
- moved to Sisyphus for Slic3r (by dd@ request)

* Thu Oct 10 2013 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1
- initial import by package builder

