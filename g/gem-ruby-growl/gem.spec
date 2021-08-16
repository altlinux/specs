%define        gemname ruby-growl

Name:          gem-ruby-growl
Version:       4.1
Release:       alt1
Summary:       A pure-ruby growl notifier for UDP and GNTP growl protocols
License:       BSD 3-clause
Group:         Development/Ruby
Url:           https://github.com/drbrain/ruby-growl
Vcs:           https://github.com/drbrain/ruby-growl.git
Packager:      Pavel Skrylev <majioa@altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(uuid) >= 2.3.5 gem(uuid) < 3
BuildRequires: gem(minitest) >= 5.14 gem(minitest) < 6
BuildRequires: gem(rdoc) >= 4.0 gem(rdoc) < 7
BuildRequires: gem(hoe) >= 3.22 gem(hoe) < 4

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency rdoc >= 6.1.1,rdoc < 7
Requires:      gem(uuid) >= 2.3.5 gem(uuid) < 3
Provides:      gem(ruby-growl) = 4.1


%description
A pure-ruby growl notifier for UDP and GNTP growl protocols. ruby-growl allows
you to perform Growl notifications from machines without growl installed (for
example, non-OSX machines).

What is growl? Growl is a really cool "global notification system originally for
Mac OS X".

You can receive Growl notifications on various platforms and send them from any
machine that runs Ruby.

OS X: http://growl.info Windows: http://www.growlforwindows.com/gfw/ Linux:
http://github.com/mattn/growl-for-linux

ruby-growl also contains a command-line notification tool named 'growl'. It is
almost completely option-compatible with growlnotify. (All except for -p is
supported, use --priority instead.)


%package       -n growl
Version:       4.1
Release:       alt1
Summary:       A pure-ruby growl notifier for UDP and GNTP growl protocols executable(s)
Summary(ru_RU.UTF-8): Исполнямка для самоцвета ruby-growl
Group:         Other
BuildArch:     noarch

Requires:      gem(ruby-growl) = 4.1

%description   -n growl
A pure-ruby growl notifier for UDP and GNTP growl protocols executable(s).

A pure-ruby growl notifier for UDP and GNTP growl protocols. ruby-growl allows
you to perform Growl notifications from machines without growl installed (for
example, non-OSX machines).

What is growl? Growl is a really cool "global notification system originally for
Mac OS X".

You can receive Growl notifications on various platforms and send them from any
machine that runs Ruby.

OS X: http://growl.info Windows: http://www.growlforwindows.com/gfw/ Linux:
http://github.com/mattn/growl-for-linux

ruby-growl also contains a command-line notification tool named 'growl'. It is
almost completely option-compatible with growlnotify. (All except for -p is
supported, use --priority instead.)

%description   -n growl -l ru_RU.UTF-8
Исполнямка для самоцвета ruby-growl.


%package       -n gem-ruby-growl-doc
Version:       4.1
Release:       alt1
Summary:       A pure-ruby growl notifier for UDP and GNTP growl protocols documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета ruby-growl
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(ruby-growl) = 4.1

%description   -n gem-ruby-growl-doc
A pure-ruby growl notifier for UDP and GNTP growl protocols documentation
files.

A pure-ruby growl notifier for UDP and GNTP growl protocols. ruby-growl allows
you to perform Growl notifications from machines without growl installed (for
example, non-OSX machines).

What is growl? Growl is a really cool "global notification system originally for
Mac OS X".

You can receive Growl notifications on various platforms and send them from any
machine that runs Ruby.

OS X: http://growl.info Windows: http://www.growlforwindows.com/gfw/ Linux:
http://github.com/mattn/growl-for-linux

ruby-growl also contains a command-line notification tool named 'growl'. It is
almost completely option-compatible with growlnotify. (All except for -p is
supported, use --priority instead.)

%description   -n gem-ruby-growl-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета ruby-growl.


%package       -n gem-ruby-growl-devel
Version:       4.1
Release:       alt1
Summary:       A pure-ruby growl notifier for UDP and GNTP growl protocols development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета ruby-growl
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(ruby-growl) = 4.1
Requires:      gem(minitest) >= 5.14 gem(minitest) < 6
Requires:      gem(rdoc) >= 4.0 gem(rdoc) < 7
Requires:      gem(hoe) >= 3.22 gem(hoe) < 4

%description   -n gem-ruby-growl-devel
A pure-ruby growl notifier for UDP and GNTP growl protocols development
package.

A pure-ruby growl notifier for UDP and GNTP growl protocols. ruby-growl allows
you to perform Growl notifications from machines without growl installed (for
example, non-OSX machines).

What is growl? Growl is a really cool "global notification system originally for
Mac OS X".

You can receive Growl notifications on various platforms and send them from any
machine that runs Ruby.

OS X: http://growl.info Windows: http://www.growlforwindows.com/gfw/ Linux:
http://github.com/mattn/growl-for-linux

ruby-growl also contains a command-line notification tool named 'growl'. It is
almost completely option-compatible with growlnotify. (All except for -p is
supported, use --priority instead.)

%description   -n gem-ruby-growl-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета ruby-growl.


%prep
%setup

%build
%ruby_build

%install
%ruby_install

%check
%ruby_test

%files
%doc README.txt
%ruby_gemspec
%ruby_gemlibdir

%files         -n growl
%doc README.txt
%_bindir/growl

%files         -n gem-ruby-growl-doc
%doc README.txt
%ruby_gemdocdir

%files         -n gem-ruby-growl-devel
%doc README.txt


%changelog
* Tue Jun 22 2021 Pavel Skrylev <majioa@altlinux.org> 4.1-alt1
- + packaged gem with Ruby Policy 2.0
