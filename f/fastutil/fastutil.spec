%define _unpackaged_files_terminate_build 1

Name: fastutil
Version: 8.5.19
Release: alt1

Summary: Type-specific collections and algorithms for Java
License: Apache-2.0
Group: Development/Java
URL: https://fastutil.di.unimi.it/
VCS: https://github.com/vigna/fastutil.git

BuildArch: noarch

Source0: %name-%version.tar
Patch0: %name-alt.patch

BuildRequires(pre): rpm-macros-java
BuildRequires: rpm-build-java
BuildRequires: maven-local
BuildRequires: ant
BuildRequires: aqute-bnd
BuildRequires: gcc
BuildRequires: make
BuildRequires: java-11-openjdk-devel

%package core
Summary: Core subset of type-specific collections for Java
Group: Development/Java

%description
Fastutil provides type-specific maps, sets, lists, queues, and algorithms
for Java, with a small memory footprint and fast access and insertion.

%description core
Fastutil Core contains the integer, long, double, and object collections
from fastutil. It is a smaller alternative to the full fastutil artifact.

%prep
%setup -q
%patch0 -p1

%build
make -j2 sources SHELL=/bin/bash .SHELLFLAGS="-e -o pipefail -c"
ant -Dversion=%version osgi
ant -Dversion=%version pom
# The upstream split script calls jdeps, which ships beside javac in ALT and
# needs the JDK launcher libraries on the runtime path.
JDK_BIN="$(dirname "$(readlink -f "$(command -v javac)")")"
JDK_HOME="$(dirname "$JDK_BIN")"
JDK_LIB="$JDK_HOME/lib:$JDK_HOME/lib/server"
if [ -n "${LD_LIBRARY_PATH-}" ]; then
    JDK_LIB="$JDK_LIB:$LD_LIBRARY_PATH"
fi
PATH="$JDK_BIN:$PATH" \
LD_LIBRARY_PATH="$JDK_LIB" \
    ./split.sh
ant -Dversion=%version -Ddist=dist-core osgi-core pom-core

%install
%mvn_artifact pom.xml dist/lib/fastutil-%version.jar
%mvn_artifact pom-core.xml dist-core/lib/fastutil-core-%version.jar
%mvn_file it.unimi.dsi:fastutil fastutil/fastutil
%mvn_file it.unimi.dsi:fastutil-core fastutil-core/fastutil-core
%mvn_package it.unimi.dsi:fastutil fastutil
%mvn_package it.unimi.dsi:fastutil-core fastutil-core
%mvn_install

%files -f .mfiles-fastutil
%doc CHANGES LICENSE-2.0

%files core -f .mfiles-fastutil-core

%changelog
* Wed Oct 28 2026 Ivan Khanas <xeno@altlinux.org> 8.5.19-alt1
- Initial build for ALT.
