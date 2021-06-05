Group: Development/Java
BuildRequires: /proc rpm-build-java
BuildRequires: jpackage-11-compat
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global pretty_name NeuroML2

# Upstream used this as the release tag:
# https://github.com/NeuroML/jNeuroML/tags
%global gittag NMLv2.0

%global _description \
This repository contains the NeuroML 2 Schema, the ComponentType definitions in\
LEMS and a number of example files in NeuroML 2 and LEMS files for running\
simulations.\
\
For more details on LEMS and NeuroML 2 see:\
\
Robert C. Cannon, Padraig Gleeson, Sharon Crook, Gautham Ganapathy, Boris\
Marin, Eugenio Piasini and R. Angus Silver, LEMS: A language for expressing\
complex biological models in concise and hierarchical form and its use in\
underpinning NeuroML 2, Frontiers in Neuroinformatics 2014,\
doi:10.3389/fninf.2014.00079


Name:           jneuroml-core
Version:        1.6.1
Release:        alt1_4jpp11
Summary:        The NeuroML 2 Schema and ComponentType definitions in LEMS

License:        LGPLv3
URL:            https://github.com/NeuroML/%{pretty_name}

Source0:        %{url}/archive/%{gittag}/%{name}-%{version}.tar.gz
BuildArch:      noarch

BuildRequires:  maven-local
BuildRequires:  maven-remote-resources-plugin
Source44: import.info

%description 

# NO javadocs

%_description
%package doc
Group: Development/Java
Summary:        NeuroML2 core documentation, schemas, and examples
# bootstrap.css file is ASL 2.0
License:        LGPLv3 and ASL 2.0
BuildArch: noarch

%description doc 

%_description
%prep
%setup -q -n %{pretty_name}-%{gittag}


# Remove currently unused omv/omt files
rm -fv LEMSexamples/test/.test*


%build
%mvn_build -- -Dmaven.compiler.source=1.8 -Dmaven.compiler.target=1.8 -Dmaven.javadoc.source=1.8 -Dmaven.compiler.release=8

%install
%mvn_install

%files -f .mfiles
%doc --no-dereference LICENSE.lesser
%doc README.md CONTRIBUTING.md

%files doc
%doc --no-dereference LICENSE.lesser
%doc HISTORY.md
%doc examples docs Schemas LEMSexamples NeuroML2CoreTypes


%changelog
* Sat Jun 05 2021 Igor Vlasenko <viy@altlinux.org> 1.6.1-alt1_4jpp11
- new version

