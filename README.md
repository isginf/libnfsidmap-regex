## NAME
regex - libnfsidmap plugin using regex based mapping

## SYNOPSIS
Plugin for libnfsidmap.  Uses regex to map NFSv4 names to and from ids.

## DESCRIPTION
The  regex  plugin  parses  NFSv4  user and groups names using regex to
extract the local user or group. NFSv4 names are created by adding constant
strings before and after the local user and group names.

## CONFIGURATION
The configuration for the  plugin  is  in  a  new  `[Regex]`  section  in
`/etc/idmapd.conf` that may contain lines of the form

         variable = value

The recognized variables are as follows:

### [Regex] section variables

#### User-Regex
Regular  expression  that  extracts  the local user name from an
NFSv4 name. Several expressions can be  concatenated  with  '|'.
The first match will be used.


#### Group-Regex
Regular  expression  that  extracts the local group name from an
NFSv4 name. Several expressions can be  concatenated  with  '|'.
The first match will be used.

#### Prepend-Before-User
Constant string to put before a local user name when building an
NFSv4 name.

(Default: none)

#### Append-After-User
Constant string to put after a local user name when building  an
NFSv4 name.

(Default: none)

#### Prepend-Before-Group
Constant  string  to put before a local group name when building
an NFSv4 name.

(Default: none)

#### Append-After-Group
Constant string to put before a local group name  when  building
an NFSv4 name.

(Default: none)

#### Group-Name-Prefix
Constant  string  that  is  prepended to a local group name when
converting it to an NFSv4 name. If an NFSv4 group name has  this
prefix  it  is removed when converting it to a local group name.
Is not applied if a static group mapping matches.

This allows to organize the group name space in a central directory
that is used for a central NFS4 server and use short group
names in the local directory used in organizational units.

#### Group-Map-File
File name of an INI style file containing static group mappings.

(Default: /etc/idmapd.conf)

#### Group-Map-Section
Section in the static group mapping file that contains the  mappings.
The name must be all lower case. The section name in the
file is case sensitive.

(Default: groups)

## STATIC MAPPING
The Group-Map-File and  Group-Map-Section  variables  can  be  used  to
define a section containing mappings of the form

         nfs4 group = local group

The default is to have a `[Groups]` section in the `/etc/idmapd.conf` file.

For  both the NFS4 and local group name the Group-Name-Prefix prefix is
not applied or removed.

## EXAMPLES
An example `[Regex]` and `[Groups]` section in the `/etc/idmapd.conf` file:

       [Regex]
       User-Regex = ^EXAMPLE\([^@]+)@EXAMPLE.ORG$
       Group-Regex = ^([^@]+)@EXAMPLE.ORG@EXAMPLE.ORG$|^EXAMPLE\([^@]+)@EXAMPLE.ORG$
       Prepend-Before-User = EXAMPLE
       Append-After-User = @EXAMPLE.ORG
       #Prepend-Before-Group =
       Append-After-Group = @example.org@example.org
       Group-Name-Prefix = sales-

       [Groups]
       domain users = users

## SEE ALSO
idmapd.conf(5)

## BUGS
Report bugs to <stefan.walter@inf.ethz.ch>
