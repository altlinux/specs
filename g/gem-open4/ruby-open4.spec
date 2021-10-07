%define        gemname open4

Name:          gem-open4
Version:       1.3.4
Release:       alt1.1
Summary:       Manage child processes and their IO handles easily
License:       Ruby
Group:         Development/Ruby
Url:           http://github.com/ahoward/open4
Vcs:           https://github.com/ahoward/open4.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-open4 < %EVR
Provides:      ruby-open4 = %EVR
Provides:      gem(open4) = 1.3.4


%description
Open child process with handles on pid, stdin, stdout, and stderr: manage child
processes and their io handles easily.

This library can read and update netrc files, preserving formatting including
comments and whitespace.


%package       -n gem-open4-doc
Version:       1.3.4
Release:       alt1.1
Summary:       Manage child processes and their IO handles easily documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета open4
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(open4) = 1.3.4

%description   -n gem-open4-doc
Manage child processes and their IO handles easily documentation files.

Open child process with handles on pid, stdin, stdout, and stderr: manage child
processes and their io handles easily.

This library can read and update netrc files, preserving formatting including
comments and whitespace.

%description   -n gem-open4-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета open4.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README README.erb
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-open4-doc
%doc README README.erb
%ruby_gemdocdir


%changelog
* Sat Sep 04 2021 Pavel Skrylev <majioa@altlinux.org> 1.3.4-alt1.1
- ! spec
- * to release version

* Fri Aug 02 2019 Pavel Skrylev <majioa@altlinux.org> 1.3.4-alt1
- ^ 1.3.3 -> 1.3.4
- > Ruby Policy 2.0

* Tue Sep 05 2017 Andrey Cherepanov <cas@altlinux.org> 1.3.3-alt1.1
- Rebuild with Ruby 2.4.1

* Sun Sep 25 2016 Evgeny Sinelnikov <sin@altlinux.ru> 1.3.3-alt1
- Update to latest release

* Sat Dec 08 2012 Evgeny Sinelnikov <sin@altlinux.ru> 1.3.0-alt1
- Initial build for Sisyphus
