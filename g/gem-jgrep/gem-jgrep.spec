%define        gemname jgrep

Name:          gem-jgrep
Version:       1.5.4
Release:       alt1
Summary:       Filter JSON documents with a simple logical language
License:       Apache-2.0
Group:         Development/Ruby
Url:           https://github.com/ploubser/JSON-Grep
Vcs:           https://github.com/ploubser/json-grep.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
Provides:      gem(jgrep) = 1.5.4


%description
Compare a list of json documents to a simple logical language and returns
matches as output.

JGrep is a command line tool and API for parsing JSON documents based on
logical expressions.


%package       -n jgrep
Version:       1.5.4
Release:       alt1
Summary:       Filter JSON documents with a simple logical language executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета jgrep
Group:         Other
BuildArch:     noarch

Requires:      gem(jgrep) = 1.5.4

%description   -n jgrep
Filter JSON documents with a simple logical language executable(s).

Compare a list of json documents to a simple logical language and returns
matches as output.

JGrep is a command line tool and API for parsing JSON documents based on
logical expressions.

%description   -n jgrep -l ru_RU.UTF-8
Исполнямка для самоцвета jgrep.


%package       -n gem-jgrep-doc
Version:       1.5.4
Release:       alt1
Summary:       Filter JSON documents with a simple logical language documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета jgrep
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(jgrep) = 1.5.4

%description   -n gem-jgrep-doc
Filter JSON documents with a simple logical language documentation
files.

Compare a list of json documents to a simple logical language and returns
matches as output.

JGrep is a command line tool and API for parsing JSON documents based on
logical expressions.

%description   -n gem-jgrep-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета jgrep.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.markdown
%ruby_gemspec
%ruby_gemlibdir

%files         -n jgrep
%doc README.markdown
%_bindir/jgrep

%files         -n gem-jgrep-doc
%doc README.markdown
%ruby_gemdocdir


%changelog
* Fri Sep 16 2022 Pavel Skrylev <majioa@altlinux.org> 1.5.4-alt1
- + packaged gem with Ruby Policy 2.0
