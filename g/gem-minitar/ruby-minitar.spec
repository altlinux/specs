%define        gemname minitar

Name:          gem-minitar
Version:       0.9.0.1
Release:       alt1
Summary:       Minimal pure-ruby support for POSIX tar(1) archives
License:       Ruby or BSD-2-Clause
Group:         Development/Ruby
Url:           https://github.com/halostatue/minitar/
Vcs:           https://github.com/halostatue/minitar/.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(minitest) >= 5.14 gem(minitest) < 6
BuildRequires: gem(hoe-doofus) >= 1.0 gem(hoe-doofus) < 2
BuildRequires: gem(hoe-gemspec2) >= 1.1 gem(hoe-gemspec2) < 2
BuildRequires: gem(hoe-git) >= 1.6 gem(hoe-git) < 2
BuildRequires: gem(hoe-rubygems) >= 1.0 gem(hoe-rubygems) < 2
BuildRequires: gem(minitest-autotest) >= 1.0 gem(minitest-autotest) < 2
BuildRequires: gem(rake) >= 10.0 gem(rake) < 14
BuildRequires: gem(rdoc) >= 0.0 gem(rdoc) < 7
BuildRequires: gem(hoe) >= 3.22 gem(hoe) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
%ruby_use_gem_dependency minitest >= 5.17.0,minitest < 6
%ruby_use_gem_version minitar:0.9.0.1
%ruby_use_gem_version archive-tar-minitar:0.9.0.1
%ruby_ignore_names archive-tar-minitar
Obsoletes:     ruby-minitar < %EVR
Obsoletes:     ruby-archive-tar-minitar
Provides:      ruby-minitar = %EVR
Provides:      ruby-archive-tar-minitar
Provides:      gem(minitar) = 0.9.0.1


%description
The minitar library is a pure-Ruby library that provides the ability to deal
with POSIX tar(1) archive files.

This is release 0.6, providing a number of bug fixes including a directory
traversal vulnerability, CVE-2016-10173. This release starts the migration and
modernization of the code:

* the licence has been changed to match the modern Ruby licensing scheme (Ruby
  and Simplified BSD instead of Ruby and GNU GPL);
* the minitar command-line program has been separated into the minitar-cli
  gem;
* the archive-tar-minitar gem now points to the minitar and minitar-cli gems and
  discourages its installation.

Some of these changes may break existing programs that depend on the internal
structure of the minitar library, but every effort has been made to ensure
compatibility; inasmuch as is possible, this compatibility will be maintained
through the release of minitar 1.0 (which will have strong breaking
changes).

minitar (previously called Archive::Tar::Minitar) is based heavily on code
originally written by Mauricio Julio Fernandez Pradier for the rpa-base project.


%package       -n gem-minitar-doc
Version:       0.9.0.1
Release:       alt1
Summary:       Minimal pure-ruby support for POSIX tar(1) archives documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета minitar
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(minitar) = 0.9.0.1
Obsoletes:     minitar-doc
Obsoletes:     ruby-archive-tar-minitar-doc
Provides:      minitar-doc
Provides:      ruby-archive-tar-minitar-doc

%description   -n gem-minitar-doc
Minimal pure-ruby support for POSIX tar(1) archives documentation files.

The minitar library is a pure-Ruby library that provides the ability to deal
with POSIX tar(1) archive files.

This is release 0.6, providing a number of bug fixes including a directory
traversal vulnerability, CVE-2016-10173. This release starts the migration and
modernization of the code:

* the licence has been changed to match the modern Ruby licensing scheme (Ruby
  and Simplified BSD instead of Ruby and GNU GPL);
* the minitar command-line program has been separated into the minitar-cli
  gem;
* the archive-tar-minitar gem now points to the minitar and minitar-cli gems and
  discourages its installation.

Some of these changes may break existing programs that depend on the internal
structure of the minitar library, but every effort has been made to ensure
compatibility; inasmuch as is possible, this compatibility will be maintained
through the release of minitar 1.0 (which will have strong breaking
changes).

minitar (previously called Archive::Tar::Minitar) is based heavily on code
originally written by Mauricio Julio Fernandez Pradier for the rpa-base project.

%description   -n gem-minitar-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета minitar.


%package       -n gem-minitar-devel
Version:       0.9.0.1
Release:       alt1
Summary:       Minimal pure-ruby support for POSIX tar(1) archives development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета minitar
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(minitar) = 0.9.0.1
Requires:      gem(minitest) >= 5.14 gem(minitest) < 6
Requires:      gem(hoe-doofus) >= 1.0 gem(hoe-doofus) < 2
Requires:      gem(hoe-gemspec2) >= 1.1 gem(hoe-gemspec2) < 2
Requires:      gem(hoe-git) >= 1.6 gem(hoe-git) < 2
Requires:      gem(hoe-rubygems) >= 1.0 gem(hoe-rubygems) < 2
Requires:      gem(minitest-autotest) >= 1.0 gem(minitest-autotest) < 2
Requires:      gem(rake) >= 10.0 gem(rake) < 14
Requires:      gem(rdoc) >= 0.0 gem(rdoc) < 7
Requires:      gem(hoe) >= 3.22 gem(hoe) < 4

%description   -n gem-minitar-devel
Minimal pure-ruby support for POSIX tar(1) archives development package.

The minitar library is a pure-Ruby library that provides the ability to deal
with POSIX tar(1) archive files.

This is release 0.6, providing a number of bug fixes including a directory
traversal vulnerability, CVE-2016-10173. This release starts the migration and
modernization of the code:

* the licence has been changed to match the modern Ruby licensing scheme (Ruby
  and Simplified BSD instead of Ruby and GNU GPL);
* the minitar command-line program has been separated into the minitar-cli
  gem;
* the archive-tar-minitar gem now points to the minitar and minitar-cli gems and
  discourages its installation.

Some of these changes may break existing programs that depend on the internal
structure of the minitar library, but every effort has been made to ensure
compatibility; inasmuch as is possible, this compatibility will be maintained
through the release of minitar 1.0 (which will have strong breaking
changes).

minitar (previously called Archive::Tar::Minitar) is based heavily on code
originally written by Mauricio Julio Fernandez Pradier for the rpa-base project.

%description   -n gem-minitar-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета minitar.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.rdoc
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-minitar-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-minitar-devel
%doc README.rdoc


%changelog
* Thu Sep 02 2021 Pavel Skrylev <majioa@altlinux.org> 0.9.0.1-alt1
- ^ 0.9 -> 0.9.0.1

* Tue Oct 29 2019 Pavel Skrylev <majioa@altlinux.org> 0.9-alt1
- update (^) 0.6.1 -> 0.9
- add (+) archive-tar-minitar gem and package deprecation

* Thu Aug 30 2018 Pavel Skrylev <majioa@altlinux.org> 0.6.1-alt1
- Initial build for Sisyphus
