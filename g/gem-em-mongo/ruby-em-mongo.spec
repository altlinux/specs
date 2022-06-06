%define        gemname em-mongo

Name:          gem-em-mongo
Version:       0.6.0.1
Release:       alt1
Summary:       EventMachine MongoDB Driver (based off of RMongo)
License:       MIT
Group:         Development/Ruby
Url:           https://github.com/bcg/em-mongo
Vcs:           https://github.com/bcg/em-mongo.git
Packager:      Ruby Maintainers Team <ruby@packages.altlinux.org>
BuildArch:     noarch

Source:        %name-%version.tar
BuildRequires(pre): rpm-build-ruby
BuildRequires: gem(eventmachine) >= 0.12.10 gem(eventmachine) < 2.0
BuildRequires: gem(bson) >= 1.9.2 gem(bson) < 5

%add_findreq_skiplist %ruby_gemslibdir/**/*
%add_findprov_skiplist %ruby_gemslibdir/**/*
%ruby_use_gem_dependency bson ~> 4.0
Requires:      gem(eventmachine) >= 0.12.10 gem(eventmachine) < 2.0
Requires:      gem(bson) >= 1.9.2 gem(bson) < 5
Obsoletes:     ruby-em-mongo
Provides:      ruby-em-mongo
Provides:      gem(em-mongo) = 0.6.0.1

%ruby_use_gem_version em-mongo:0.6.0.1

%description
An EventMachine client for MongoDB. Originally based on RMongo, this client aims
to be as api compatible with mongo-ruby-driver as possible.

For methods that do not retrieve data from the database the api of em-mongo
should be identical (though a subset) to the mongo-ruby-driver. This includes
the various update methods like insert, save and update (without the :safe flag,
which is handled separately) as well as find, which returns a cursor.

For operations that require IO, em-mongo always returns an EventMachine
deferrable.


%package       -n gem-em-mongo-doc
Version:       0.6.0.1
Release:       alt1
Summary:       EventMachine MongoDB Driver (based off of RMongo) documentation files
Summary(ru_RU.UTF-8): Файлы сведений для самоцвета em-mongo
Group:         Development/Documentation
BuildArch:     noarch

Requires:      gem(em-mongo) = 0.6.0.1

%description   -n gem-em-mongo-doc
EventMachine MongoDB Driver (based off of RMongo) documentation files.

An EventMachine client for MongoDB. Originally based on RMongo, this client aims
to be as api compatible with mongo-ruby-driver as possible.

For methods that do not retrieve data from the database the api of em-mongo
should be identical (though a subset) to the mongo-ruby-driver. This includes
the various update methods like insert, save and update (without the :safe flag,
which is handled separately) as well as find, which returns a cursor.

For operations that require IO, em-mongo always returns an EventMachine
deferrable.

%description   -n gem-em-mongo-doc -l ru_RU.UTF-8
Файлы сведений для самоцвета em-mongo.


%package       -n gem-em-mongo-devel
Version:       0.6.0.1
Release:       alt1
Summary:       EventMachine MongoDB Driver (based off of RMongo) development package
Summary(ru_RU.UTF-8): Файлы для разработки самоцвета em-mongo
Group:         Development/Ruby
BuildArch:     noarch

Requires:      gem(em-mongo) = 0.6.0.1
Requires:      gem(bson) >= 4.0 gem(bson) < 5

%description   -n gem-em-mongo-devel
EventMachine MongoDB Driver (based off of RMongo) development package.

An EventMachine client for MongoDB. Originally based on RMongo, this client aims
to be as api compatible with mongo-ruby-driver as possible.

For methods that do not retrieve data from the database the api of em-mongo
should be identical (though a subset) to the mongo-ruby-driver. This includes
the various update methods like insert, save and update (without the :safe flag,
which is handled separately) as well as find, which returns a cursor.

For operations that require IO, em-mongo always returns an EventMachine
deferrable.

%description   -n gem-em-mongo-devel -l ru_RU.UTF-8
Файлы для разработки самоцвета em-mongo.


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

%files         -n gem-em-mongo-doc
%doc README.rdoc
%ruby_gemdocdir

%files         -n gem-em-mongo-devel
%doc README.rdoc


%changelog
* Mon Apr 18 2022 Pavel Skrylev <majioa@altlinux.org> 0.6.0.1-alt1
- ^ 0.6.0 -> 0.6.0.1

* Wed Mar 04 2020 Pavel Skrylev <majioa@altlinux.org> 0.6.0-alt2.3
- fixed (!) spec

* Tue Sep 10 2019 Pavel Skrylev <majioa@altlinux.org> 0.6.0-alt2.2
- fixed (!) spec according to changelog rules

* Fri Jul 12 2019 Pavel Skrylev <majioa@altlinux.org> 0.6.0-alt2.1
- fixed (!) spec

* Mon Feb 18 2019 Pavel Skrylev <majioa@altlinux.org> 0.6.0-alt2
- Use Ruby Policy 2.0.

* Thu Mar 08 2018 Andrey Cherepanov <cas@altlinux.org> 0.6.0-alt1
- New version.

* Wed Oct 25 2017 Andrey Cherepanov <cas@altlinux.org> 0.5.1-alt1
- New version

* Wed Oct 18 2017 Andrey Cherepanov <cas@altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus
