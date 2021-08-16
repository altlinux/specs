%define        gemname parslet

Name:          gem-parslet
Version:       2.0.0
Release:       alt1
Summary:       Parser construction library with great error reporting in Ruby
License:       MIT
Group:         Development/Ruby
Url:           http://kschiess.github.io/parslet
Vcs:           https://github.com/kschiess/parslet.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_ignore_names website
Provides:      gem(parslet) = 2.0.0

%description
Parslet makes developing complex parsers easy. It does so by

* providing the best error reporting possible
* not generating reams of code for you to debug

Parslet takes the long way around to make your job easier. It allows for
incremental language construction. Often, you start out small, implementing
the atoms of your language first; _parslet_ takes pride in making this
possible.


%package       -n gem-parslet-doc
Version:       2.0.0
Release:       alt1
Summary:       Parser construction library with great error reporting in Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета parslet
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(parslet) = 2.0.0

%description   -n gem-parslet-doc
Parser construction library with great error reporting in Ruby documentation
files.

Parslet makes developing complex parsers easy. It does so by

* providing the best error reporting possible
* not generating reams of code for you to debug

Parslet takes the long way around to make your job easier. It allows for
incremental language construction. Often, you start out small, implementing
the atoms of your language first; _parslet_ takes pride in making this
possible.

%description   -n gem-parslet-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета parslet.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README
%ruby_gemspec
%ruby_gemlibdir

%files         -n gem-parslet-doc
%doc README
%ruby_gemdocdir


%changelog
* Tue Jul 13 2021 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- + packaged gem with Ruby Policy 2.0
