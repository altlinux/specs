%define        pkgname net-sftp

Name:          gem-%pkgname
Version:       3.0.0
Release:       alt1
Summary:       A pure Ruby implementation of the SFTP client protocol
Group:         Development/Ruby
License:       MIT
Url:           https://github.com/net-ssh/net-sftp
Vcs:           https://github.com/net-ssh/net-sftp.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(mocha)
BuildRequires: gem(net-ssh)

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-%gemname < %EVR
Provides:      ruby-%gemname = %EVR

%description
Net::SFTP is a pure-Ruby implementation of the SFTP protocol (specifically,
versions 1 through 6 of the SFTP protocol). Note that this is the "Secure File
Transfer Protocol", typically run over an SSH connection, and has nothing to
do with the FTP protocol.


%package       doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch

%description   doc
Documentation files for %gemname gem.

%description   doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         doc
%ruby_gemdocdir


%changelog
* Wed Jul 08 2020 Pavel Skrylev <majioa@altlinux.org> 3.0.0-alt1
- > Ruby Policy 2.0
- ^ 2.1.2 -> 3.0.0
- ! spec tags

* Tue Sep 04 2018 Andrey Cherepanov <cas@altlinux.org> 2.1.2-alt1
- New version.

* Tue Jul 24 2018 Andrey Cherepanov <cas@altlinux.org> 2.0.3-alt2.2
- Rebuild with new Ruby autorequirements.

* Thu Dec 06 2012 Led <led@altlinux.ru> 2.0.3-alt2.1
- Rebuilt with ruby-1.9.3-alt1
- disabled check

* Sat Dec 12 2009 Alexey I. Froloff <raorn@altlinux.org> 2.0.3-alt2
- Fixed file conflict in doc subpackage with net-ssh and net-scp docs
- Enabled tests

* Sat Dec 05 2009 Igor Zubkov <icesik@altlinux.org> 2.0.3-alt1
- build for Sisyphus


