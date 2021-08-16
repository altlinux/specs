%define        gemname retriable

Name:          gem-retriable
Version:       3.1.2.1
Release:       alt1
Summary:       Retriable is an simple DSL to retry failed code blocks with randomized exponential backoff
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/kamui/retriable
Vcs:           https://github.com/kamui/retriable.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(bundler) >= 0 gem(bundler) < 3

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Obsoletes:     ruby-retriable < %EVR
Provides:      ruby-retriable = %EVR
Provides:      gem(retriable) = 3.1.2.1

%ruby_use_gem_version retriable:3.1.2.1

%description
Retriable is a simple DSL to retry failed code blocks with randomized
exponential backoff time intervals. This is especially useful when interacting
external APIs, remote services, or file system calls.


%package       -n gem-retriable-doc
Version:       3.1.2.1
Release:       alt1
Summary:       Retriable is an simple DSL to retry failed code blocks with randomized exponential backoff documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета retriable
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(retriable) = 3.1.2.1

%description   -n gem-retriable-doc
Retriable is an simple DSL to retry failed code blocks with randomized
exponential backoff documentation files.

Retriable is a simple DSL to retry failed code blocks with randomized
exponential backoff time intervals. This is especially useful when interacting
external APIs, remote services, or file system calls.

%description   -n gem-retriable-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета retriable.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.md
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-retriable-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Wed Jun 02 2021 Pavel Skrylev <majioa@altlinux.org> 3.1.2.1-alt1
- > Ruby Policy 2.0
- ^ 3.1.2 -> 3.1.2.1

* Wed Nov 14 2018 Pavel Skrylev <majioa@altlinux.org> 3.1.2-alt3
- Gemify correctly 3.1.2

* Fri Jul 06 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.2-alt2
- Rebuild for correct gemspec file name.

* Thu Jul 05 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.2-alt1
- New version.
- Package as gem.

* Fri May 25 2018 Andrey Cherepanov <cas@altlinux.org> 3.1.1-alt1
- Initial build for Sisyphus
