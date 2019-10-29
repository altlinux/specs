%define        pkgname minitar

Name:          ruby-%pkgname
Version:       0.9
Release:       alt1
Summary:       Minimal pure-ruby support for POSIX tar(1) archives.
License:       Simplified BSD
Group:         Development/Ruby
Url:           https://github.com/halostatue/minitar/
%vcs           https://github.com/halostatue/minitar/.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

Provides:      ruby-archive-tar-minitar
Obsoletes:     ruby-archive-tar-minitar

%description
The minitar library is a pure-Ruby library that provides the ability to deal
with POSIX tar(1) archive files.

This is release 0.6, providing a number of bug fixes including a directory
traversal vulnerability, CVE-2016-10173. This release starts the migration and
modernization of the code:

* the licence has been changed to match the modern Ruby licensing scheme (Ruby
  and Simplified BSD instead of Ruby and GNU GPL);
* the minitar command-line program has been separated into the minitar-cli gem;
* the archive-tar-minitar gem now points to the minitar and minitar-cli gems
  and discourages its installation.

Some of these changes may break existing programs that depend on the internal
structure of the minitar library, but every effort has been made to ensure
compatibility; inasmuch as is possible, this compatibility will be maintained
through the release of minitar 1.0 (which will have strong breaking changes).

minitar (previously called Archive::Tar::Minitar) is based heavily on code
originally written by Mauricio Julio Fernandez Pradier for the rpa-base project.


%package       -n gem-%pkgname-doc
Summary:       Documentation files for %gemname gem
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета %gemname
Group:         Development/Documentation
BuildArch:     noarch
Provides:      %pkgname-doc
Obsoletes:     %pkgname-doc
Provides:      ruby-archive-tar-minitar-doc
Obsoletes:     ruby-archive-tar-minitar-doc


%description   -n gem-%pkgname-doc
Documentation files for %gemname gem.

%description   -n gem-%pkgname-doc -l ru_RU.UTF8
Файлы сведений для самоцвета %gemname.


%prep
%setup

%build
%ruby_build --ignore=archive-tar-minitar

%install
%ruby_install

%check
%ruby_test

%files         -n ruby-%pkgname
%doc README*
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-%pkgname-doc
%ruby_gemdocdir


%changelog
* Tue Oct 29 2019 Pavel Skrylev <majioa@altlinux.org> 0.9-alt1
- update (^) 0.6.1 -> 0.9
- add (+) archive-tar-minitar gem and package deprecation

* Thu Aug 30 2018 Pavel Skrylev <majioa@altlinux.org> 0.6.1-alt1
- Initial build for Sisyphus
