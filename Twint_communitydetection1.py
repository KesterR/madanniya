# initialise Lists and Dicts of member orgs of We Exist Alliance and other Syrian CSOs

list_memberorgs = [
'basmehzeitooneh',
'STJ_SYRIA_ENG',
'impactcsrd',
'WomenNowForDev',
'DawlatyOrg',
'DOZ_Int',
'Rethink_Rebuild',
'Childprotectsyr',
'PelCivil',
'PLHRsyria1',
'TheSyriaCmpgn',
'snhr',
'sawafordaid',
'actcentre',
'SyrianCenter',
'SyrianLDP',
'SyrieMDL',
'TDA_SY',
'Urnammu3',
'VDC_Syria']
# print("list_memberorgs")
# print(list_memberorgs)

list_CSOs_notYetMembers = [ #as list
'shaml_coalition',
'MosaicInit',
'CitizensSyria',
'ASML_medialibre',
'SJAC_info',
'SyrianACD',
'AdoptRevolution',
'SyrianNGOAllian',
'irada_program']
# print("list_CSOs_notYetMembers")
# print(list_CSOs_notYetMembers)

dict_memberorgs = {
'basmehzeitooneh':'basmehzeitooneh',
'SyriansforTruthandJustice':'STJ_SYRIA_ENG',
'Impact': 'impactcsrd',
'WomenForDevelopmentNow': 'WomenNowForDev',
'Dawlaty': 'DawlatyOrg',
'DOZ': 'DOZ_Int',
'RethinkRebuild': 'Rethink_Rebuild',
'HurrasChildProtection': 'Childprotectsyr',
'PelCivil': 'PelCivil',
'PalestinianLeague': 'PLHRsyria1',
'TheSyriaCampaign': 'TheSyriaCmpgn',
'SN4HR': 'snhr',
'SAWA': 'sawafordaid',
'ACT': 'actcentre',
'SyrianCentre': 'SyrianCenter',
'SyrianLegalDevelopmentProg': 'SyrianLDP',
'SyrieMDL':'SyrieMDL',
'TheDayAfter': 'TDA_SY',
'Urnammu': 'Urnammu3',
'VDC': 'VDC_Syria'}
# print("dict_memberorgs")
# print(dict_memberorgs)

dict_CSOs_notYetMembers = {
'Shaml': 'shaml_coalition',
'Mosaic': 'MosaicInit',
'CitizensSyria': 'CitizensSyria',
'ASML': 'ASML_medialibre',
'SJAC': 'SJAC_info',
'SyrianACD': 'SyrianACD',
'AdoptRevolution': 'AdoptRevolution',
'SyrianNGOAlliance': 'SyrianNGOAllian',
'Irada': 'irada_program'}
# print("dict_CSOs_notYetMembers")
# print(dict_CSOs_notYetMembers)

# get follower-following adjacencies for memberorgs
    # G is a DiGraph class of object
    # c is assigned to a function
    # i is an iterator and a String object in G

import networkx as nx
import twint

G = nx.Graph()
G.add_nodes_from(dict_memberorgs)

c = twint.Config()
c.Hide_output = True

for i in G:
    c.Username = i
    #c.User_full = True
    c.Store_object = True
    twint.run.Followers(c)
    followers = twint.output.follows_list
G.add_nodes_from(followers)
print(G.__len__())

#fails at line 91 because the size of G changes during iteration 

#    for j in Followers:
 #       G.add_edges_from(j)

    # print(G)
    # G.add_edge(i, c.adj())

# Create Association Matrix of Followers and Following accounts of WeExist Member Orgs

# find Mutual Follows
# from https://colab.research.google.com/drive/1AOXQxkOWbq7KEHWVBRiOrYhTOSg3QTqq#scrollTo=1lZrarvrzsVT

# c.Pandas = True
 # twint.run.Following(c)

#  Following_df = twint.storage.panda.Follow_df
# list_of_following = Following_df['following'][username]

#  def intersection(lst1, lst2):
#    return list(set(lst1) & set(lst2))

#  mufos = intersection(list_of_followers, list_of_following)
#  return mufos

# mufos = mutuals(username)