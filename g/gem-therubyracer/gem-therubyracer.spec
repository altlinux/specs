%define        gemname therubyracer

Name:          gem-therubyracer
Version:       0.12.3
Release:       alt1
Summary:       Embed the V8 JavaScript interpreter into Ruby
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/cowboyd/therubyracer
Vcs:           https://github.com/cowboyd/therubyracer.git
Packager:      Pavel Skrylev <majioa@altlinux.org>

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rubysl) >= 0
BuildRequires: gem(rake) >= 0
BuildRequires: gem(rspec) >= 3.5.0
BuildRequires: gem(rake-compiler) >= 0
BuildRequires: gem(gem-compiler) >= 0
BuildRequires: gem(ref) >= 0
BuildRequires: gem(libv8) >= 3.16.14.15
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(libv8) >= 9
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_use_gem_dependency libv8 >= 8.4.255.0,libv8 < 9
Requires:      gem(ref) >= 0
Requires:      gem(libv8) >= 3.16.14.15
Conflicts:     gem(libv8) >= 9
Provides:      gem(therubyracer) = 0.12.3


%description
Call JavaScript code and manipulate JavaScript objects from Ruby. Call Ruby code
and manipulate Ruby objects from JavaScript.


%package       -n gem-therubyracer-doc
Version:       0.12.3
Release:       alt1
Summary:       Embed the V8 JavaScript interpreter into Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета therubyracer
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(therubyracer) = 0.12.3

%description   -n gem-therubyracer-doc
Embed the V8 JavaScript interpreter into Ruby documentation files.

Call JavaScript code and manipulate JavaScript objects from Ruby. Call Ruby code
and manipulate Ruby objects from JavaScript.

%description   -n gem-therubyracer-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета therubyracer.


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
%ruby_gemextdir

%files         -n gem-therubyracer-doc
%doc README.md
%ruby_gemdocdir


%changelog
* Sat Dec 02 2023 Pavel Skrylev <majioa@altlinux.org> 0.12.3-alt1
- + packaged gem with Ruby Policy 2.0 without devel
