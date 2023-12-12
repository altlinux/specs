%define        _unpackaged_files_terminate_build 1
%define        gemname ref

Name:          gem-ref
Version:       2.0.0
Release:       alt1
Summary:       Library that implements weak, soft, and strong references in Ruby
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/ruby-concurrency/ref
Vcs:           https://github.com/ruby-concurrency/ref.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 10.3.2
BuildRequires: gem(rake-compiler) >= 0.9.5
BuildRequires: gem(test-unit) >= 3.0.9
BuildRequires: gem(rspec) >= 3.1.0
BuildRequires: gem(coveralls) >= 0.7.3
BuildRequires: gem(yard) >= 0.8.7.4
BuildRequires: gem(inch) >= 0.4.6
BuildRequires: gem(redcarpet) >= 3.1.2
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rake-compiler) >= 2
BuildConflicts: gem(test-unit) >= 4
BuildConflicts: gem(rspec) >= 4
BuildConflicts: gem(coveralls) >= 1
BuildConflicts: gem(yard) >= 1
BuildConflicts: gem(inch) >= 1
BuildConflicts: gem(redcarpet) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.1.0,rake < 14
%ruby_use_gem_dependency test-unit >= 3.3.5,test-unit < 4
%ruby_use_gem_dependency rspec >= 3.10.0,rspec < 4
%ruby_use_gem_dependency rake-compiler >= 1.1.2,rake-compiler < 2
%ruby_use_gem_dependency coveralls >= 0.8.23,coveralls < 1
%ruby_use_gem_dependency yard >= 0.9.34,yard < 1
%ruby_use_gem_dependency inch >= 0.8.0,inch < 1
%ruby_use_gem_dependency redcarpet >= 3.5.1.1,redcarpet < 4
Provides:      gem(ref) = 2.0.0


%description
Library that implements weak, soft, and strong references in Ruby that work
across multiple runtimes (MRI,Jruby and Rubinius). Also includes implementation
of maps/hashes that use references and a reference queue.


%package       -n gem-ref-doc
Version:       2.0.0
Release:       alt1
Summary:       Library that implements weak, soft, and strong references in Ruby documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ref
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ref) = 2.0.0

%description   -n gem-ref-doc
Library that implements weak, soft, and strong references in Ruby documentation
files.

Library that implements weak, soft, and strong references in Ruby that work
across multiple runtimes (MRI,Jruby and Rubinius). Also includes implementation
of maps/hashes that use references and a reference queue.

%description   -n gem-ref-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ref.


%package       -n gem-ref-devel
Version:       2.0.0
Release:       alt1
Summary:       Library that implements weak, soft, and strong references in Ruby development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ref
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ref) = 2.0.0
Requires:      gem(rake) >= 10.3.2
Requires:      gem(rake-compiler) >= 0.9.5
Requires:      gem(test-unit) >= 3.0.9
Requires:      gem(rspec) >= 3.1.0
Requires:      gem(coveralls) >= 0.7.3
Requires:      gem(yard) >= 0.8.7.4
Requires:      gem(inch) >= 0.4.6
Requires:      gem(redcarpet) >= 3.1.2
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rake-compiler) >= 2
Conflicts:     gem(test-unit) >= 4
Conflicts:     gem(rspec) >= 4
Conflicts:     gem(coveralls) >= 1
Conflicts:     gem(yard) >= 1
Conflicts:     gem(inch) >= 1
Conflicts:     gem(redcarpet) >= 4

%description   -n gem-ref-devel
Library that implements weak, soft, and strong references in Ruby development
package.

Library that implements weak, soft, and strong references in Ruby that work
across multiple runtimes (MRI,Jruby and Rubinius). Also includes implementation
of maps/hashes that use references and a reference queue.

%description   -n gem-ref-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ref.


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

%files         -n gem-ref-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-ref-devel
%doc README.md


%changelog
* Sat Dec 02 2023 Pavel Skrylev <majioa@altlinux.org> 2.0.0-alt1
- + packaged gem with Ruby Policy 2.0
