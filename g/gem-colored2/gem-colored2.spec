%define        gemname colored2

Name:          gem-colored2
Version:       3.1.2.1
Release:       alt0.1
Summary:       Add even more color to your life
License:       MIT
Group:         Development/Ruby
Url:           http://github.com/kigster/colored2
Vcs:           https://github.com/kigster/colored2.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
%if_with check
BuildRequires: gem(rake) >= 10.0
BuildRequires: gem(rspec) >= 3.4
BuildRequires: gem(codeclimate-test-reporter) >= 0
BuildConflicts: gem(rake) >= 14
BuildConflicts: gem(rspec) >= 4
%endif

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rake >= 13.0.1,rake < 14
Provides:      gem(colored2) = 3.1.2.1

%ruby_use_gem_version colored2:3.1.2.1

%description
This is a heavily modified fork of http://github.com/defunkt/colored gem, with
many sensible pull requests combined. Since the authors of the original gem no
longer support it, this might, perhaps, be considered a good
alternative.

Simple gem that adds various color methods to String class, and can be used as
follows:

require 'colored2'

puts 'this is red'.red puts 'this is red with a yellow background'.red.on.yellow
puts 'this is red with and italic'.red.italic puts 'this is green
bold'.green.bold << ' and regular'.green puts 'this is really bold blue on white
but reversed'.bold.blue.on.white.reversed puts 'this is regular, but '.red! <<
'this is red '.yellow! << ' and yellow.'.no_color! puts ('this is regular, but
'.red! do 'this is red '.yellow! do ' and yellow.'.no_color! end end)


%package       -n gem-colored2-doc
Version:       3.1.2.1
Release:       alt0.1
Summary:       Add even more color to your life documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета colored2
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(colored2) = 3.1.2.1

%description   -n gem-colored2-doc
Add even more color to your life documentation files.

This is a heavily modified fork of http://github.com/defunkt/colored gem, with
many sensible pull requests combined. Since the authors of the original gem no
longer support it, this might, perhaps, be considered a good
alternative.

Simple gem that adds various color methods to String class, and can be used as
follows:

require 'colored2'

puts 'this is red'.red puts 'this is red with a yellow background'.red.on.yellow
puts 'this is red with and italic'.red.italic puts 'this is green
bold'.green.bold << ' and regular'.green puts 'this is really bold blue on white
but reversed'.bold.blue.on.white.reversed puts 'this is regular, but '.red! <<
'this is red '.yellow! << ' and yellow.'.no_color! puts ('this is regular, but
'.red! do 'this is red '.yellow! do ' and yellow.'.no_color! end end)

%description   -n gem-colored2-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета colored2.


%package       -n gem-colored2-devel
Version:       3.1.2.1
Release:       alt0.1
Summary:       Add even more color to your life development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета colored2
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(colored2) = 3.1.2.1
Requires:      gem(rake) >= 10.0
Requires:      gem(rspec) >= 3.4
Requires:      gem(codeclimate-test-reporter) >= 0
Conflicts:     gem(rake) >= 14
Conflicts:     gem(rspec) >= 4

%description   -n gem-colored2-devel
Add even more color to your life development package.

This is a heavily modified fork of http://github.com/defunkt/colored gem, with
many sensible pull requests combined. Since the authors of the original gem no
longer support it, this might, perhaps, be considered a good
alternative.

Simple gem that adds various color methods to String class, and can be used as
follows:

require 'colored2'

puts 'this is red'.red puts 'this is red with a yellow background'.red.on.yellow
puts 'this is red with and italic'.red.italic puts 'this is green
bold'.green.bold << ' and regular'.green puts 'this is really bold blue on white
but reversed'.bold.blue.on.white.reversed puts 'this is regular, but '.red! <<
'this is red '.yellow! << ' and yellow.'.no_color! puts ('this is regular, but
'.red! do 'this is red '.yellow! do ' and yellow.'.no_color! end end)

%description   -n gem-colored2-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета colored2.


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

%files         -n gem-colored2-doc
%doc README.md
%ruby_gemdocdir

%files         -n gem-colored2-devel
%doc README.md


%changelog
* Fri Jan 27 2023 Pavel Skrylev <majioa@altlinux.org> 3.1.2.1-alt0.1
- ^ 3.1.2 -> 3.1.2.1

* Fri May 06 2022 Pavel Skrylev <majioa@altlinux.org> 3.1.2-alt1
- + packaged gem with Ruby Policy 2.0
