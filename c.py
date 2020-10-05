class Controller:
    ca_dict = {}

    def make_well_sequencedness(self,graph_name):

        ca = self.ca_dict.get(graph_name)

        ret = self.well_sequencedness_conditions(ca)

        if ret == None:
            result = ['Verified: Well-sequenced']
            return [result]
        else:
            result = ['Verified: NO Well-sequenced, not verified in ' + ret]
            return [result]

   def make_well_branchedness(self,graph_name):

        ca = self.ca_dict.get(graph_name)


        res1 = self.well_branchedness_first_condition(ca.edges,ca.states)
        
        if res1 != None:
            result = ['Verified: NO Well-branched in first condition: ' + res1]
            return [result]


        res2 = self.well_branchedness_second_condition(ca.edges,ca.states,ca.participants)

        if res2 != None:
            result = ['Verified: NO Well-branched in second condition: ' + res2]
            return [result]

        res3 = self.well_branchedness_second_condition(ca.edges,ca.states,ca.participants)

        if res3 != None:
            result = ['Verified: NO Well-branched in third condition: ' + res3]
            return [result]

        else:
            result = ['Verified: Well-branched']
            return [result]

    def make_well_formedness(self.graph_name):

        resultWS = self.make_well_sequencedness(graph_name)

        if resultWS[0] == 'Verified: Well-sequenced':

            resultWB = self.make_well_branchedness(graph_name)

            if resultWB[0] == 'Verified: Well-branched':

                result = ['Verified: Well-formed']
                return [result]
                
            return [resultWB[0]]

        return [resultWS[0]]