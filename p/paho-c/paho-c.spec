%define _unpackaged_files_terminate_build 1
%define abiversion 1
%def_disable static

Name: paho-c
Version: 1.3.13
Release: alt1

Summary: Eclipse Paho C Client Library for the MQTT Protocol
License: BSD-3-Clause and EPL-2.0
Group: System/Libraries
Url: https://www.eclipse.org/paho
VCS: https://github.com/eclipse/paho.mqtt.c

# Source-url: https://github.com/eclipse/paho.mqtt.c/archive/refs/tags/v%{version}.tar.gz
Source: %name-%version.tar

Requires: lib%name-%abiversion = %EVR

BuildRequires: cmake
BuildRequires: doxygen
BuildRequires: graphviz
BuildRequires: libssl-devel

%description
MQTT is a light weight publish/subscribe messaging protocol, originally created
by IBM and Arcom (later to become part of Eurotech) around 1998. MQTT is an
OASIS standard.

%package -n libpaho-mqtt%abiversion
Summary: Eclipse Paho MQTT C client - shared libraries
Group: System/Libraries

%description -n libpaho-mqtt%abiversion
This libraries enable applications to connect to an MQTT broker to publish
messages, and to subscribe to topics and receive published messages.

%package -n libpaho-mqtt-devel
Summary: Eclipse Paho MQTT C client - shared libraries
Group: System/Libraries
Requires: libpaho-mqtt%abiversion = %EVR

%description -n libpaho-mqtt-devel
This libraries enable applications to connect to an MQTT broker to publish
messages, and to subscribe to topics and receive published messages.

This package contains files for development and static libraries.

%package doc
Summary: MQTT C Client development kit documentation
Group: Development/C
BuildArch: noarch

%description doc
Development documentation files for the the Paho MQTT C Client.

%prep
%setup

%build
%cmake -DPAHO_WITH_SSL=TRUE \
    -DPAHO_BUILD_DOCUMENTATION=FALSE \
    -DPAHO_BUILD_SAMPLES=FALSE \
    -DPAHO_ENABLE_TESTING=FALSE \
    -DPAHO_ENABLE_CPACK=FALSE \
%if_enabled static
	-DPAHO_BUILD_STATIC=TRUE
%else
	-DPAHO_BUILD_STATIC=FALSE
%endif
%cmake_build

%install
%cmakeinstall_std

%files -n libpaho-mqtt%abiversion
%_libdir/*.so.%version
%_libdir/*.so.1

%files -n libpaho-mqtt-devel
%_bindir/MQTTVersion
%_includedir/*
%_libdir/*.so
%_libdir/cmake/*

%files doc
%doc LICENSE edl-v10 epl-v20
%_defaultdocdir/*

%changelog
* Mon Apr 01 2024 Dmitrii Fomchenkov <sirius@altlinux.org> 1.3.13-alt1
- Initial build for ALT Linux
